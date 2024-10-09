# Copyright (C) 2015-2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

class Firefox(Dependency):
    name = "firefox"
    default = "128.3.0esr"
    tags = ["browser_firefox"]
    exes = [{
        "version": "128.3.0esr",
        "url": "https://download.mozilla.org/?product=firefox-esr-msi-latest-ssl&os=win64&lang=en-US",
        "sha1": "c5118ca76f0cf6ecda5d2b9292bf191525c9627a",
    }]

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)

        self.a.execute("msiexec /i C:\\%s /passive /norestart" % self.filename)
        self.a.remove("C:\\%s" % self.filename)

class Firefox41(Firefox, Dependency):
    """Backwards compatibility"""
    name = "firefox_41"
