@echo off
title Deletiing Outdated Updates

net stop wuauserv
cd %Windir%\SoftwareDistribution
del /f /s /q Download
net start wuauserv
exit