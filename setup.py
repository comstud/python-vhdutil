# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2011, Chris Behrens <cbehrens@codestud.com>
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied. See the License for the specific language governing
#    permissions and limitations under the License.

from distutils.core import setup

#package_dir = {'' : 'src'}

setup(name='python-vhdutil',
        version='0.0.1',
        description='Utility to manipulate VHD files',
        author='Chris Behrens',
        author_email='cbehrens@codestud.com',
        url='http://www.github.com/comstud/python-vhdutil',
        requires=['libvhd'],
        scripts=['src/vhdutil.py'],
        license='Apache 2.0')
