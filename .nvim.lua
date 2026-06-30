-- Project-local Neovim configuration for Interview Prep

local keymap = vim.keymap

-- Helper to run command in a split terminal and auto-scroll/focus it
local function run_in_terminal(cmd)
  vim.cmd("split")
  vim.cmd("terminal " .. cmd)
  -- Automatically enter insert mode or start scrolling to bottom
  vim.cmd("normal! G")
end

-- Keymap options
local opts = { silent = true }

-- 1. Run the current test file
opts.desc = "[Test] Run current test file"
keymap.set("n", "<leader>tf", function()
  local file = vim.fn.expand("%")
  if file:match("test_.*%.py$") or file:match("%.py$") then
    run_in_terminal(".venv/bin/pytest " .. file)
  else
    print("Current file is not a python file!")
  end
end, opts)

-- 2. Run all tests in the current directory (exercise folder)
opts.desc = "[Test] Run tests in current directory"
keymap.set("n", "<leader>td", function()
  local dir = vim.fn.expand("%:p:h")
  run_in_terminal(".venv/bin/pytest " .. dir)
end, opts)

-- 3. Run all tests in the repository
opts.desc = "[Test] Run all tests in workspace"
keymap.set("n", "<leader>ta", function()
  run_in_terminal(".venv/bin/pytest")
end, opts)

-- 4. Run pyrefly type-check on the current file
opts.desc = "[LSP] Run pyrefly check on current file"
keymap.set("n", "<leader>tc", function()
  local file = vim.fn.expand("%")
  run_in_terminal(".venv/bin/pyrefly check " .. file)
end, opts)

print("🎓 [Prep Workspace] Local test keymaps loaded: <leader>tf (file), <leader>td (directory), <leader>ta (all), <leader>tc (type-check)")
