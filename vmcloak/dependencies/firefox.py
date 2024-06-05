# Copyright (C) 2015-2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

class Firefox(Dependency):
    name = "firefox"
    default = "41.0.2"
    tags = ["browser_firefox"]
    exes = [{
        "version": "41.0.2",
        "url": "https://cuckoo.sh/vmcloak/Firefox_Setup_41.0.2.exe",
        "sha1": "c5118ca76f0cf6ecda5d2b9292bf191525c9627a",
    }, {
        "version": "60.0.2",
        "url": "https://cuckoo.sh/vmcloak/firefox_60_0_2.exe",
        "sha1": "565c5ddca3e4acbc30a550f312d3a1a7fd8d8bce",
    }, {
        "version": "63.0.3",
        "url": "https://cuckoo.sh/vmcloak/firefox_63_0_3.exe",
        "sha1": "c5f03fc93aebd2db9da14ba6eb1f01e98e18d95b",
    }, {
        "version": "latest",
        "url": "https://download-installer.cdn.mozilla.net/pub/firefox/releases/123.0/win64/en-US/Firefox%20Setup%20123.0.exe",
        "sha1": "75f85bbc5934c7f7ff4c4794a9c8d8ad45e79040",
    }]

    def run(self):
        self.upload_dependency("C:\\Firefox_Setup_123.0.exe")
        self.a.execute("C:\\Firefox_Setup_123.0.exe -ms")
        self.a.remove("C:\\Firefox_Setup_123.0.exe")

class Firefox41(Firefox, Dependency):
    """Backwards compatibility"""
    name = "firefox_41"
