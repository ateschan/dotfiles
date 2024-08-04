# For Debugging type pydevd and request a code-completion.
# Choose the first suggestion and you will see something like:
#    import sys;sys.path.append(r/some/path/eclipse/plugins/org.python.pydev.core_6.5.0.201809011628/pysrc)
#    import pydevd;pydevd.settrace()
# Place pydevd.settrace() before the line you want the debugger to stop and
# start debugging your extension (right click on project -> Debug As -> LibreOffice extension)
# You need to manually switch to debug view in Eclipse then.

import sys
import os
import uno, unohelper
from com.sun.star.task import XJobExecutor
from com.sun.star.document import XEventListener
from com.sun.star.awt import XActionListener
from com.sun.star.text.TextContentAnchorType import AT_PARAGRAPH
from com.sun.star.lang import IllegalArgumentException
from com.sun.star.uno import RuntimeException

import draw
import code128
from extensioncore import *


SUPPORTED_LANGUAGES = ('en', 'da', 'de', 'fr', 'hu', 'ja', 'nl', 'sh', 'sr', 'zh')    # first one is default

com_sun_star_awt_SystemPointer_ARROW = uno.getConstantByName( 'com.sun.star.awt.SystemPointer.ARROW' )
com_sun_star_awt_SystemPointer_REFHAND = uno.getConstantByName( 'com.sun.star.awt.SystemPointer.REFHAND' )
com_sun_star_drawing_TextHorizontalAdjust_CENTER = 1

class Barcode( ComponentBase, XActionListener ):
    SUPPORTED_LANGUAGES = SUPPORTED_LANGUAGES

    def __init__( self, *args ):
        ComponentBase.__init__(self, *args)
        self.barlengthmodify = 100
        self.barwidthmodify = 100

    def insert( self ):
        dlg = self.createdialog( 'Barcode' )
        getattr( dlg, self.config.LastBarcodeType ).State = True
        dlg.WithChecksum.State = self.config.LastChecksum
        dlg.HeightModify.Text = self.config.HeightModify
        dlg.WidthModify.Text = self.config.WidthModify
        dlg.PositionX.Text = self.config.PositionX
        dlg.PositionY.Text = self.config.PositionY

        while True:
            ok = dlg.execute()
            if not ok:
                return
            for codetype in self.CODETYPES:
                if getattr( dlg, codetype ).State:
                    break
            value = dlg.CodeField.Text
            value = getattr( self, 'validate_%s'%codetype )( value, dlg.WithChecksum.State )
            # empty field somehow appears as "&652.Barcode.CodeField.Text"
            if value is not None and value != "" and value != "&652.Barcode.CodeField.Text":
                self.config.LastBarcodeType = codetype
                self.config.LastChecksum = dlg.WithChecksum.State
                self.config.HeightModify = dlg.HeightModify.Text
                self.config.WidthModify = dlg.WidthModify.Text
                self.config.PositionX = dlg.PositionX.Text
                self.config.PositionY = dlg.PositionY.Text
                self.config.commitChanges()
                self.barlengthmodify = dlg.HeightModify.Text
                self.barwidthmodify = dlg.WidthModify.Text
                group = getattr( self, 'draw_%s'%codetype )( value, dlg.WithChecksum.State )
                draw.setpos( group, self.config.PositionX, self.config.PositionY )
                return
# Removes spaces and minus sign (-) characters from the input value
    def remove_spaces( self, value ):
        nonspace = []
        for v in value:
            if v not in (' ', '-'):
                nonspace.append( v )
        value = ''.join( nonspace )
        return value
    def validate_just_digits( self, value ):
        for c in value:
            if c not in '0123456789':
                self.box( self.localize( 'only-decimal' ) )
                return None
        return value
    def validate_UPCA( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 11:
            self.box( self.localize( 'UPC-A-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 11:
            self.box( self.localize( 'UPC-A-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 12:
            self.box( self.localize( 'UPC-A-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_EAN13( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 12:
            self.box( self.localize( 'EAN-13-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 12:
            self.box( self.localize( 'EAN-13-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 13:
            self.box( self.localize( 'EAN-13-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_ISBN13( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 12:
            self.box( self.localize( 'ISBN-13-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 12:
            self.box( self.localize( 'ISBN-13-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 13:
            self.box( self.localize( 'ISBN-13-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_Bookland( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 9:
            self.box( self.localize( 'ISBN-10-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 9:
            self.box( self.localize( 'ISBN-10-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 10:
            self.box( self.localize( 'ISBN-10-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_JAN( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 10:
            self.box( self.localize( 'JAN-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 10:
            self.box( self.localize( 'JAN-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 11:
            self.box( self.localize( 'JAN-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_UPCE( self, value, add_checksum ):
        value = self.remove_spaces( value )
        value = self.validate_just_digits( value )
        if value is None:
            return None
        if add_checksum:
            if len( value ) == 6:
                return '0' + value
            elif len( value ) == 7:
                if value[0] != '0':
                    self.box( self.localize( 'UPC-E-zero' ) )
                    return None
                return value
            else:
                self.box( self.localize( 'UPC-E-length-checksum' ) )
                return None
        else:
            if len( value ) == 7:
                self.box( self.localize( 'UPC-E-length-almost' ) )
                return None
            elif len( value ) == 8:
                if value[0] != '0':
                    self.box( self.localize( 'UPC-E-zero' ) )
                    return None
                return value
            else:
                self.box( self.localize( 'UPC-E-length' ) )
                return None
    def validate_EAN8( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) != 7:
            self.box( self.localize( 'EAN-8-length-checksum' ) )
            return None
        elif not add_checksum and len( value ) == 7:
            self.box( self.localize( 'EAN-8-length-almost' ) )
            return None
        elif not add_checksum and len( value ) != 8:
            self.box( self.localize( 'EAN-8-length' ) )
            return None
        return self.validate_just_digits( value )
    def validate_STANDARD2OF5( self, value, add_checksum ):
        value = self.remove_spaces( value )
        return self.validate_just_digits( value )
    def validate_INTERLEAVED2OF5( self, value, add_checksum ):
        value = self.remove_spaces( value )
        if add_checksum and len( value ) % 2 == 0:
            self.box( self.localize( 'INTERLEAVED2OF5-length-even' ) )
            return None
        elif not add_checksum and len( value ) % 2 == 1:
            self.box( self.localize( 'INTERLEAVED2OF5-length-odd' ) )
            return None
        return self.validate_just_digits( value )
    def validate_CODE128( self, value, add_checksum ):
        if code128.encode( value ) is None:
            self.box( self.localize( 'CODE-128-can-not-be-encoded' ) )
            return None
        return value
    CODETYPES = 'EAN13', 'ISBN13', 'Bookland', 'UPCA', 'JAN', 'EAN8', 'UPCE', 'STANDARD2OF5', 'INTERLEAVED2OF5', 'CODE128'
    UPC_TABLE = {
        '0':    '0001101',
        '1':    '0011001',
        '2':    '0010011',
        '3':    '0111101',
        '4':    '0100011',
        '5':    '0110001',
        '6':    '0101111',
        '7':    '0111011',
        '8':    '0110111',
        '9':    '0001011',
        }
    UPC_REVERSED_TABLE = dict( [(k, v.replace( '0', 'X' ).replace( '1', '0' ).replace( 'X', '1' )) for (k, v) in list(UPC_TABLE.items())] )
    EAN_L_TABLE = UPC_TABLE
    EAN_G_TABLE = {
        '0':    '0100111',
        '1':    '0110011',
        '2':    '0011011',
        '3':    '0100001',
        '4':    '0011101',
        '5':    '0111001',
        '6':    '0000101',
        '7':    '0010001',
        '8':    '0001001',
        '9':    '0010111',
        }
    EAN_R_TABLE = UPC_REVERSED_TABLE
    EAN_LG_TABLE = {        # the first digit and this table are used to decide when to use the L and G tables on the left side in EAN-13
        '0':    'LLLLLL',
        '1':    'LLGLGG',
        '2':    'LLGGLG',
        '3':    'LLGGGL',
        '4':    'LGLLGG',
        '5':    'LGGLLG',
        '6':    'LGGGLL',
        '7':    'LGLGLG',
        '8':    'LGLGGL',
        '9':    'LGGLGL',
        }
    # the UPC-E parity encoding table is the inverse of EAN_LG_TABLE except for index 0
    # the checksum digit and this table are used to decide when to use the L and G tables in UPC-E
    UPCE_LG_TABLE = {
        '0':    'GGGLLL',
        '1':    'GGLGLL',
        '2':    'GGLLGL',
        '3':    'GGLLLG',
        '4':    'GLGGLL',
        '5':    'GLLGGL',
        '6':    'GLLLGG',
        '7':    'GLGLGL',
        '8':    'GLGLLG',
        '9':    'GLLGLG',
        }
    CODE_2OF5_TABLE = {
        '0':    'nnWWn',
        '1':    'WnnnW',
        '2':    'nWnnW',
        '3':    'WWnnn',
        '4':    'nnWnW',
        '5':    'WnWnn',
        '6':    'nWWnn',
        '7':    'nnnWW',
        '8':    'WnnWn',
        '9':    'nWnWn',
        }
    def drawbars( self, code, x, barlength, barwidth ):
        '''
        Draws the bars for the given binary code string.
        Black bars will be drawn for 1's and nothing for 0's.
        x is the x coordinate to draw at.
        drawbars returns the code (as a list of lists of coordinates)
        '''
        x0 = x
        bars = []
        for b in code:
            if b == '1':
                bars.append( [(x, 0), (x + barwidth, 0), (x + barwidth, -barlength), (x, -barlength)] )
            x += barwidth
        return bars

    BARWIDTH = 80
    BARLENGTH = 3000
    LONGBAREXTRALENGTH = 400

    def getDrawPage(self):
        page = None
        if self.isWriter():
            page = self.getcomponent().DrawPage
        elif self.isCalc():
            page = self.getcontroller().ActiveSheet.DrawPage
        elif self.isImpress() or self.isDraw():
            page = self.getcontroller().CurrentPage
        return page

    def drawcode( self, code, barlength = None, barwidth = None):
        '''
        Draws the code described in the code parameter.
        code is a list of pairs of the form (binary, meta) where
        binary is a string made up of 1's and 0's (1's representing black bars) and
        meta is a string that is either
            '' (empty string), signifying that there is nothing to be done
            'long', signifying that the bars should be drawn longer than usual
            or a single character string that will be printed under the bars.
        drawcode returns a Draw object that is a group of the bars and the text.
        '''
        if barlength is None:
            barlength = self.BARLENGTH
        if barwidth is None:
            barwidth = self.BARWIDTH
        barwidth =  int (int (barwidth) * int (self.barwidthmodify) / 100)
        normalbarlength =  int (int (barlength) * int (self.barlengthmodify) / 100)
        longbarlength = int ( (barlength + self.LONGBAREXTRALENGTH) * int (self.barlengthmodify) / 100 )
        doc = self.getcomponent()
        page = self.getDrawPage()
        group = self.ctx.ServiceManager.createInstance( 'com.sun.star.drawing.ShapeCollection' )
        bars = []
        x = 0
        for binary, meta in code:
            if meta == 'long':
                barlength = longbarlength
            else:
                barlength = normalbarlength
            bars.extend( self.drawbars( binary, x, barlength , barwidth ) )
            w = barwidth * len( binary )
            if len( meta ) == 1:
                shape = draw.createShape( doc, page, 'Text' )
                shape.String = meta
                shape.TextAutoGrowWidth = True
                shape.TextAutoGrowHeight = True
                shape.CharFontName = "Liberation Mono"
                shape.CharHeight = int (20 * int (self.barwidthmodify) / 100)
                shape.TextHorizontalAdjust = com_sun_star_drawing_TextHorizontalAdjust_CENTER
                if (self.isWriter()):
                    shape.AnchorType = AT_PARAGRAPH
                if self.isWriter() or self.isDraw() or self.isImpress():
                    pos_x = x - 200;
                else: # Calc
                    pos_x = x
                draw.setpos( shape, pos_x, normalbarlength, w , shape.Size.Height )
                group.add( shape )
            x += w
        shape = draw.createPolygon( doc, page, bars, color = draw.RGB( 0, 0, 0 ) )
        shape.LineStyle = 0
        if (self.isWriter()):
            shape.AnchorType = AT_PARAGRAPH
            # Writer needs some positioning hack due to DrawPage differences
            last = self.config.LastBarcodeType
            if last == 'EAN13' or last == 'ISBN13' or last == 'Bookland' or last == 'UPCA' \
                or last == 'JAN' or last == 'UPCE':
                draw.setpos(shape, 300, 0)
            elif last == 'EAN8' or last == 'STANDARD2OF5':
                draw.setpos(shape, -200, 0)
            else: # INTERLEAVED2OF5, CODE128
                draw.setpos(shape, 0, 0)
        group.add( shape )
        return page.group( group )
    def draw_UPCA( self, value, add_checksum ):
        if add_checksum:
            value += self.checksum_UPCA( value )
        code = []
        code.append( ('000000', value[0]) )    # the first digit goes into the quiet zone
        code.append( ('101', 'long') )
        code.append( (self.UPC_TABLE[value[0]], 'long') )
        for digit in value[1:6]:
            code.append( (self.UPC_TABLE[digit], digit) )
        code.append( ('01010', 'long') )
        for digit in value[6:-1]:
            code.append( (self.UPC_REVERSED_TABLE[digit], digit) )
        code.append( (self.UPC_REVERSED_TABLE[value[-1]], 'long') )
        code.append( ('101', 'long') )
        code.append( ('000000', value[-1]) )    # the last digit goes into the quiet zone
        return self.drawcode( code )
    def draw_UPCE( self, value, add_checksum ):
        def UPCEtoA( value ):
            if value[5] in '012':
                return '0%s%s0000%s'%(value[:2], value[5], value[2:5])
            elif value[5] == '3':
                return '0%s00000%s'%(value[:3], value[3:5])
            elif value[5] == '4':
                return '0%s00000%s'%(value[:4], value[4:5])
            else:
                return '0%s0000%s'%(value[:5], value[5])
        first = value[0]
        value = value[1:]
        if add_checksum:
            checksum = self.checksum_UPCA( UPCEtoA( value ) )
        else:
            checksum = value[-1]
            value = value[:-1]
        code = []
        code.append( ('000000', first) )
        code.append( ('101', 'long') )
        for digit, table in zip( value, self.UPCE_LG_TABLE[checksum] ):
            if table == 'L':
                code.append( (self.EAN_L_TABLE[digit], digit) )
            elif table == 'G':
                code.append( (self.EAN_G_TABLE[digit], digit) )
        code.append( ('010101', 'long') )
        code.append( ('000000', checksum) )
        return self.drawcode( code, barlength = 5000 )
    def draw_EAN13( self, value, add_checksum):
        if add_checksum:
            value += self.checksum_EAN13( value )
        first = value[0]
        value = value[1:]
        code = []
        code.append( ('000000', first) )
        code.append( ('101', 'long') )
        for digit, table in zip( value[:6], self.EAN_LG_TABLE[first] ):
            if table == 'L':
                code.append( (self.EAN_L_TABLE[digit], digit) )
            elif table == 'G':
                code.append( (self.EAN_G_TABLE[digit], digit) )
        code.append( ('01010', 'long') )
        for digit in value[6:]:
            code.append( (self.EAN_R_TABLE[digit], digit) )
        code.append( ('101', 'long') )
        return self.drawcode( code )
    def draw_EAN8( self, value, add_checksum ):
        if add_checksum:
            value += self.checksum_EAN8( value )
        code = []
        code.append( ('101', 'long') )
        for digit in value[:4]:
            code.append( (self.EAN_L_TABLE[digit], digit) )
        code.append( ('01010', 'long') )
        for digit in value[4:]:
            code.append( (self.EAN_R_TABLE[digit], digit) )
        code.append( ('101', 'long') )
        return self.drawcode( code, barlength = 5000 )
    def draw_ISBN13( self, value, add_checksum ):
        code = self.draw_EAN13( value, add_checksum )
        if add_checksum:
            value += self.checksum_EAN13( value )
        return self.add_text_above( code, 'ISBN %s-%s-%s'%(value[:3], self.separate_ISBN( value[3:12] ), value[12]) )
    def draw_Bookland( self, value, add_checksum ):
        if not add_checksum:
            check = value[-1]
            value = value[:-1]
        else:
            check = self.checksum_ISBN( value )
        code = self.draw_EAN13( '978' + value, True )
        return self.add_text_above( code, 'ISBN %s-%s'%(self.separate_ISBN( value ), check) )
    def draw_JAN( self, value, add_checksum ):
        return self.draw_EAN13( '49' + value, add_checksum )
    def draw_STANDARD2OF5( self, value, add_checksum ):
        if add_checksum:
            value += self.checksum_STANDARD2OF5( value )
        code = []
        code.append( ('11011010', 'long') )
        for digit in value:
            dcode = []
            for c in self.CODE_2OF5_TABLE[digit]:
                if c == 'W':
                    dcode.append( '1110' )
                else:
                    dcode.append( '10' )
            code.append( (''.join( dcode ), digit) )
        code.append( ('11010110', 'long' ) )
        return self.drawcode( code )
    def draw_INTERLEAVED2OF5( self, value, add_checksum ):
        if add_checksum:
            value += self.checksum_STANDARD2OF5( value )
        code = []
        code.append( ('1010', 'short') )
        for i in range( 0, len( value ), 2 ):
            for bar, space in zip( self.CODE_2OF5_TABLE[value[i]], self.CODE_2OF5_TABLE[value[i + 1]] ):
                if bar == 'W':
                    code.append( ('111', 'short') )
                else:
                    code.append( ('1', 'short') )
                if space == 'W':
                    code.append( ('000', 'short') )
                else:
                    code.append( ('0', 'short') )
        code.append( ('11101', 'short' ) )
        barcode = self.drawcode( code )
        return self.add_text_above( barcode, value, 5500 )     # place text under bars
    def draw_CODE128( self, value, add_checksum ):
        encoded = code128.encode( value )
        code = [(code128.encode( value ), 'short')]
        barcode = self.drawcode( code, barwidth = 60 )
        return self.add_text_above( barcode, value, offset = 5500 )    # place text under bars

    def separate_ISBN( self, code ):
        if '0' <= code[0] <= '7':
            group = code[0]
            code = code[1:]
        elif '80' <= code[:2] <= '94':
            group = code[:2]
            code = code[2:]
        elif '950' <= code[:3] <= '993':
            group = code[:3]
            code = code[3:]
        elif '9940' <= code[:4] <= '9989':
            group = code[:4]
            code = code[4:]
        elif '99900' <= code[:5] <= '99999':
            group = code[:5]
            code = code[5:]
        else:
            assert False, 'unless there are letters in the code this is not reachable'

        # the file for publisher ranges comes from http://www.isbn-international.org/converter/ranges.js
        with open(self.path + '/ranges.js') as ranges_file:
            for l in ranges_file:
                if l.startswith( 'gi.area%s.pubrange'%group ):
                    ranges = l.split( '"' )[1]
                    for r in ranges.split( ';' ):
                        start, end = r.split( '-' )
                        if start <= code <= end:
                            publisher = code[:len( start )]
                            title = code[len( start ):]
                            return '-'.join( (group, publisher, title) )
                    return '-'.join( (group, code) )
        return '-'.join( (group, publisher, title) )

    def add_text_above( self, code, text, offset = 0 ):
        offset = int (offset / 4 + int (offset/2) * int (self.barlengthmodify) / 100)
        doc = self.getcomponent()
        page = self.getDrawPage()
        group = self.ctx.ServiceManager.createInstance( 'com.sun.star.drawing.ShapeCollection' )
        group.add( code )
        shape = draw.createShape( doc, page, 'Text' )
        shape.String = text
        shape.TextAutoGrowWidth = True
        shape.TextAutoGrowHeight = True
        shape.CharFontName = "Liberation Mono"
        shape.CharHeight = int (20 * int (self.barwidthmodify) / 100)
        shape.TextHorizontalAdjust = com_sun_star_drawing_TextHorizontalAdjust_CENTER
        if (self.isWriter()):
            shape.AnchorType = AT_PARAGRAPH

        draw.setpos( shape, (code.Size.Width - shape.Size.Width) / 2, 0 - 1000 + offset )
        group.add( shape )

        return page.group( group )

    def checksum_UPCA( self, code ):
        '''
        From Wikipedia:

            1. Add the digits in the odd-numbered positions (first, third, fifth, etc.) together and multiply by three.
            2. Add the digits in the even-numbered positions (second, fourth, sixth, etc.) to the result.
            3. Find the result modulo 10 (i.e. the remainder when the result is divided by 10).
            4. If the result is not zero, subtract the result from ten.
        '''

        check = 0
        for i in range( len( code ) ):
            if i % 2 == 1:
                check += int( code[i] )
            else :
                check += 3 * int( code[i] )
        check %= 10
        if check != 0:
            check = 10 - check
        return str( check )
    def checksum_EAN13( self, code ):
        '''
        Same as the UPC-A checksum except it is reversed with respect to even-odd positions.
        '''
        return self.checksum_UPCA( '0' + code )
    checksum_EAN8 = checksum_UPCA
    def checksum_ISBN( self, code ):
        '''
        The 2001 edition of the official manual of the International ISBN Agency says that
        the ISBN-10 check digit -- which is the last digit of the ten-digit ISBN --
        must range from 0 to 10 (the symbol X is used instead of 10)
        and must be such that the sum of all the ten digits,
        each multiplied by the integer weight, descending from 10 to 1,
        is a multiple of the number 11.

        ISBN-13 uses the EAN-13 checksum.
        '''
        sum = 0
        for i in range( 9 ):
            sum += int( code[i] ) * (10 - i)
        check = (-sum) % 11
        if check == 10:
            return 'X'
        else:
            return str( check )
    def checksum_STANDARD2OF5( self, code ):
        '''
        An often used scheme for calculating the checksum of 2 of 5 codes. Note that it is not based on a specification, just customs.
        '''
        if len( code ) % 2 == 1:
            return self.checksum_UPCA( code )
        else:
            return self.checksum_UPCA( '0' + code )
    # XActionListener
    def actionPerformed( self, event ):
        try:
            getattr( self, 'on_action_' + event.Source.Model.Name )()
        except:
            debugexception()

    # Override execute method from extensioncore
    def execute( self, args ):
        try:
            args = unprops(args)
        except Exception:
            debugexception()

        if 'Action' not in args:
            super().execute(args)
            return

        # Enable API Mode (no msg boxes)
        self.isAPIMode = True

        if args['Action'] == "InsertBarcode":
            if 'BarcodeType' not in args:
                raise IllegalArgumentException('"BarcodeType" missing!', self, 0)
            barcodeType = args['BarcodeType']
            if barcodeType not in self.CODETYPES:
                raise IllegalArgumentException("Invalid BarcodeType '{}' Valid types: {}".format(barcodeType, ', '.join(self.CODETYPES)), self, 0)

            if 'BarcodeValue' not in args:
                raise IllegalArgumentException('"BarcodeValue" missing!', self, 0)
            barcodeValue = str(args['BarcodeValue'])
            if not barcodeValue:
                raise IllegalArgumentException('Empty or invalid "BarcodeValue" given.', self, 0)

            if 'WidthScale' in args:
                self.barwidthmodify = int(args['WidthScale'])
                if self.barwidthmodify < 1:
                    raise IllegalArgumentException('"WidthScale" must be > 0!', self, 0)
            if 'HeightScale' in args:
                self.barlengthmodify = int(args['HeightScale'])
                if self.barlengthmodify < 1:
                    raise IllegalArgumentException('"HeightScale" must be > 0!', self, 0)
            positionX = 5000
            if 'PositionX' in args:
                positionX = args['PositionX']
            positionY = 5000
            if 'PositionY' in args:
                positionY = args['PositionY']
            addChecksum = True
            if 'BarcodeAddChecksum' in args:
                addChecksum = args['BarcodeAddChecksum']
            if 'TargetComponent' in args:
                self.targetComponent = args['TargetComponent']

            self.insertBarcodeAPI(barcodeType, barcodeValue, addChecksum, positionX, positionY)
        else:
            raise IllegalArgumentException('No valid "Action" provided.', self, 0)

    def insertBarcodeAPI(self, codetype, value, addChecksum, posX, posY):
        value = getattr(self, 'validate_%s'%codetype)(value, addChecksum)
        if value is None:
            raise RuntimeException('Error validating codetype ' + codetype, self.ctx)

        group = getattr(self, 'draw_%s'%codetype)(value, addChecksum)
        draw.setpos(group, posX, posY)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    Barcode,
    "org.libreoffice.Barcode",
    ("com.sun.star.task.JobExecutor","com.sun.star.task.Job"))
