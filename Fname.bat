@echo off
setlocal enableDelayedExpansion
for %%F in (*0*.jpg) do (
  set "name=%%F"
  ren "!name!" "!name:0=f!"
)