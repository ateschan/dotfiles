return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        asm_lsp = {
          mason = false,
        },
        lua_ls = {
          mason = false,
        },
        harper_ls = {
          mason = false,
        },
      },
    },
  },
}
