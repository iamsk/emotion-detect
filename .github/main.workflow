workflow "deploy" {
  resolves = ["server"]
  on = "push"
}

action "server" {
  uses = "appleboy/ssh-action@master"
  secrets = [
    "HOST",
    "KEY",
  ]
  args = [
    "--user",
    "ubuntu",
    "--script",
    "'ls -al'",
  ]
}
