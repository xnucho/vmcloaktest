# Copyright (C) 2015-2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

class Firefox(Dependency):
    name = "firefox"
    default = "115.16.0esr"
    tags = ["browser_firefox"]
    exes = [{
        "version": "115.16.0esr",
        "url": "https://ftp.mozilla.org/pub/firefox/releases/115.16.0esr/win64/en-US/Firefox%20Setup%20115.16.0esr.msi",
    },{
        "version": "128.3.0esr",
        "url": "https://ftp.mozilla.org/pub/firefox/releases/128.3.0esr/win64/en-US/Firefox%20Setup%20128.3.0esr.msi",
    }]

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)

        self.a.execute("msiexec /i C:\\%s /passive /norestart" % self.filename)
        self.a.remove("C:\\%s" % self.filename)

class Firefox41(Firefox, Dependency):
    """Backwards compatibility"""
    name = "firefox_41"
