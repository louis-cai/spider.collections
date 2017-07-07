# 分析sign生成算法

## 涉及到阿里安全加密SDK

---
# com.android.icredit.base.BaseH5Pullctivity.class.b()

    String str = SdkHelper.a().c().a(new String[] { Constants.g, l + "", Constants.f });
    this.c.put("sign", str);

  
---
##  SdkHelper.().c().a()
Constants.g    deviceId
l              timestamp
## Constants.f

---------------------------------------------

#  Constants.f
com.android.icredit.AppApplication.class.onCreate()

Constants.f = localSecurityCipher.decryptString("437ujsOTfJqeBJwxtDebKUlsJIHeg2aD+qH+3Dur/iOIqrOdJciw8SB1WcAlVEvE", "00510944-78f5-4d1b-99a2-91c119a80edb");


## localSecurityCipher.decryptString

---
# localSecurityCipher.decryptString
com.alibaba.wireless.security.jaq.SecurityCipher.class.decryptString

paramString1 = SecurityGuardManager.getInstance(this.a).getStaticDataEncryptComp().staticSafeDecrypt(16, paramString2, paramString1, "0335");
return paramString1;

## staticSafeDecrypt

---

# staticSafeDecrypt

public String staticSafeDecrypt(int paramInt, String paramString1, String paramString2, String paramString3)
    throws SecException
  {
    if ((paramString1 != null) && (paramString1.length() > 0) && (paramInt >= 0) && (paramInt < 19) && (paramString2 != null) && (paramString2.length() > 0)) {
      return b(paramInt, paramString1.getBytes(), paramString2, paramString3);
    }
    throw new SecException("", 301);
  }
  
## b

---

# b

 private String b(int paramInt, byte[] paramArrayOfByte, String paramString1, String paramString2)
  {
    paramArrayOfByte = a(2, 1, paramInt, paramArrayOfByte, paramString1.getBytes(), paramString2);
    if (paramArrayOfByte != null) {
      try
      {
        paramArrayOfByte = new String(paramArrayOfByte, "UTF-8");
        return paramArrayOfByte;
      }
      catch (UnsupportedEncodingException paramArrayOfByte) {}
    }
    return null;
  }

## a
---

# a

 private byte[] a(int paramInt1, int paramInt2, int paramInt3, byte[] paramArrayOfByte1, byte[] paramArrayOfByte2, String paramString)
  {
    return (byte[])this.a.getRouter().doCommandNative(10601, new int[] { paramInt3, paramInt1, paramInt2 }, new String[] { paramString }, new byte[][] { paramArrayOfByte1, paramArrayOfByte2 }, null);
  }
 
 
## doCommandNative

---

# doCommandNative

package com.alibaba.wireless.security.mainplugin;
public class a
  implements IRouterComponent
{
  private JNICLibrary a = null;
  
  public Object doCommandNative(int paramInt, int[] paramArrayOfInt, String[] paramArrayOfString, Object[] paramArrayOfObject1, Object[] paramArrayOfObject2)
  {
    return this.a.doCommandNative(paramInt, paramArrayOfInt, paramArrayOfString, paramArrayOfObject1, paramArrayOfObject2);
  }
}

## this.a.doCommandNative

---

# this.a.doCommandNative

C++  JNICLibrary



--------------------------------------------



#  SdkHelper.().c().a()

package com.android.icredit.utils;

public class EncryptImpl

  public String a(String... paramVarArgs)
  {
    StringBuffer localStringBuffer = new StringBuffer();
    int j = paramVarArgs.length;
    int i = 0;
    while (i < j)
    {
      localStringBuffer.append(paramVarArgs[i]);
      i += 1;
    }
    try
    {
      paramVarArgs = new SecuritySignature(this.b).sign(localStringBuffer.toString(), "00510944-78f5-4d1b-99a2-91c119a80edb");
      return paramVarArgs;
    }
    catch (JAQException paramVarArgs)
    {
      Logger.c("EncryptImpl", this.b.getString(2131165470) + paramVarArgs.getErrorCode());
    }
    return null;
  }
  

## sign()

---

# sign()

package com.alibaba.wireless.security.jaq;
SecuritySignature

 public String sign(String paramString1, String paramString2)
    throws JAQException
  {
    HashMap localHashMap = new HashMap();
    localHashMap.put("INPUT", paramString1);
    paramString1 = new SecurityGuardParamContext();
    paramString1.appKey = paramString2;
    paramString1.paramMap = localHashMap;
    paramString1.requestType = 3;
    try
    {
      paramString1 = SecurityGuardManager.getInstance(this.a).getSecureSignatureComp().signRequest(paramString1, "0335");
      return paramString1;
    }
    catch (SecException paramString1)
    {
      paramString1.printStackTrace();
      throw new JAQException(paramString1.getErrorCode());
    }
  }

## signRequest()

---

# signRequest()

package com.alibaba.wireless.security.a.h;
public class a
  implements 

  public String signRequest(SecurityGuardParamContext paramSecurityGuardParamContext, String paramString)
    throws SecException
  {
    if ((paramSecurityGuardParamContext == null) || (paramSecurityGuardParamContext.paramMap == null)) {
      return null;
    }
    return this.a.a(paramSecurityGuardParamContext, paramString, true);
  }

## this.a.a()

---

# this.a.a()

package com.taobao.wireless.security.adapter.b;
public class b

 public String a(SecurityGuardParamContext paramSecurityGuardParamContext, String paramString, boolean paramBoolean)
    throws SecException
  {
    int i = 2;
    String str = paramSecurityGuardParamContext.appKey;
    Map localMap = paramSecurityGuardParamContext.paramMap;
    a.a locala = a.a.j[paramSecurityGuardParamContext.requestType];
    paramSecurityGuardParamContext = null;
    switch (1.a[locala.ordinal()])
    {
    default: 
      i = 0;
    }
    while ((paramSecurityGuardParamContext != null) && (i != 0))
    {
      return a(paramSecurityGuardParamContext, i, str, locala.ordinal(), paramString);
      paramSecurityGuardParamContext = a(localMap);
      continue;
      i = 1;
      paramSecurityGuardParamContext = b(localMap);
      continue;
      paramSecurityGuardParamContext = c(localMap);
    }
    throw new SecException("", 601);
  }

## a() b() c()

---
# a()
# b()
# c()

package com.taobao.wireless.security.adapter.b;
public class b


  private String[] a(Map paramMap)
    throws SecException
  {
    if ((paramMap != null) && (paramMap.size() != 2))
    {
      String.format("Input map size invalid : required size is \"%d\" and actual size is \"%d\"", new Object[] { Integer.valueOf(2), Integer.valueOf(paramMap.size()) });
      throw new SecException("", 601);
    }
    String str = (String)paramMap.get("INPUT");
    paramMap = (String)paramMap.get("SEEDKEY");
    paramMap = ((com.alibaba.wireless.security.a.k.a)this.a.getInterface(IStaticKeyEncryptComponent.class)).a(paramMap);
    if ((str != null) && (!"".equals(str)) && (paramMap != null) && (!"".equals(paramMap))) {
      return new String[] { str, paramMap };
    }
    if ((str == null) || ("".equals(str)))
    {
      String.format("Input map value invalid : key \"%1s\" not exits or the relative value is empty", new Object[] { "INPUT" });
      throw new SecException("", 601);
    }
    throw new SecException("", 606);
  }

  private String[] b(Map paramMap)
    throws SecException
  {
    if ((paramMap != null) && (paramMap.size() != 1))
    {
      String.format("Input map size invalid : required size is \"%d\" and actual size is \"%d\"", new Object[] { Integer.valueOf(1), Integer.valueOf(paramMap.size()) });
      throw new SecException("", 601);
    }
    paramMap = (String)paramMap.get("INPUT");
    if ((paramMap != null) && (!"".equals(paramMap))) {
      return new String[] { paramMap };
    }
    String.format("Input map value invalid : key \"%1s\" not exits or the relative value is empty", new Object[] { "INPUT" });
    throw new SecException("", 601);
  }
  
  private String[] c(Map paramMap)
    throws SecException
  {
    if ((paramMap != null) && ((paramMap.size() < 1) || (paramMap.size() > 2)))
    {
      String.format("Input map size invalid : required size is 1 OR 2 and actual size is \"%d\"", new Object[] { Integer.valueOf(paramMap.size()) });
      throw new SecException("", 601);
    }
    Object localObject = "";
    if (paramMap.size() == 2)
    {
      String str = (String)paramMap.get("ATLAS");
      if (str != null)
      {
        localObject = str;
        if (str.length() > 0) {}
      }
      else
      {
        throw new SecException("", 601);
      }
    }
    paramMap = (String)paramMap.get("INPUT");
    if (!com.taobao.wireless.security.adapter.common.a.a(new String[] { paramMap })) {
      return new String[] { paramMap, localObject };
    }
    String.format("Input map value invalid : some key not exits or the relative value is empty", new Object[0]);
    throw new SecException("", 601);
  }