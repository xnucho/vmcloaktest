# Copyright (C) 2015-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.
# Chrome Dependency submitted by Jason Lewis.
# https://dl.google.com/dl/chrome/install/googlechromestandaloneenterprise.msi

from vmcloak.abstract import Dependency


class Chrome(Dependency):
    name = "chrome"
    default = "109.0.5414.165"
    tags = ["browser_chrome"]
    exes = [{
        "version": "109.0.5414.165",
        "url": "https://archive.org/download/chrome-109-Win7-8/Chrome%20109%20%28Enterprise%29%20x64.msi",
    }, {
        "version": "latest",
        "arch": "x86",
        "urls": [
            "https://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise.msi"
        ],
    }, {
        "version": "latest",
        "arch": "amd64",
        "urls": [
            "https://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise64.msi"
        ],
    }]

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)

        # https://support.google.com/chrome/a/answer/6350036
        # this is not working properly :(
        self.a.execute(
            "reg add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Google\\Update\" "
            "/v UpdateDefault /t REG_DWORD /d 0 /f"
        )

        self.a.execute("msiexec /i C:\\%s /passive /norestart" % self.filename)
        self.a.remove("C:\\%s" % self.filename)

        # https://www.chromium.org/administrators/turning-off-auto-updates
        # this is not working properly :(
        self.a.execute(
            "reg add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Google\\Update\" "
            "/v AutoUpdateCheckPeriodMinutes /t REG_DWORD /d 0 /f"
        )
