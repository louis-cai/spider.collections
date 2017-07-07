# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import jnius_config
import os

_class_path = os.path.abspath('.') + '/jar/com.android.icredit_dumped_11-dex2jar.jar'

print _class_path
os.environ['CLASSPATH'] = _class_path

# jnius_config.set_classpath('.', _class_path)


from jnius import autoclass

SecExceptionCode = autoclass('com.alibaba.wireless.security.SecExceptionCode')
# SecurityCipher = autoclass('com.alibaba.wireless.security.jaq.SecurityCipher')
# SecuritySignature = autoclass('com.alibaba.wireless.security.jaq.SecuritySignature')
#
#
# sc = SecurityCipher()
# ss = SecuritySignature(None)
