local keymap = vim.keymap

local function run_in_terminal(cmd)
  vim.cmd("split")
  vim.cmd("terminal " .. cmd)
  vim.cmd("normal! G")
end

local opts = { silent = true }

opts.desc = "[Test] Run current test file"
keymap.set("n", "<leader>tf", function()
  local file = vim.fn.expand("%")
  if file:match("%.py$") then
    run_in_terminal(".venv/bin/pytest " .. file)
  else
    print("Current file is not a Python file")
  end
end, opts)

opts.desc = "[Test] Run tests in current directory"
keymap.set("n", "<leader>td", function()
  local dir = vim.fn.expand("%:p:h")
  run_in_terminal(".venv/bin/pytest " .. dir)
end, opts)

opts.desc = "[Test] Run all tests in workspace"
keymap.set("n", "<leader>ta", function()
  run_in_terminal(".venv/bin/pytest")
end, opts)

opts.desc = "[LSP] Run pyrefly check on current file"
keymap.set("n", "<leader>tc", function()
  local file = vim.fn.expand("%")
  run_in_terminal(".venv/bin/pyrefly check " .. file)
end, opts)
