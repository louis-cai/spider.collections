com.langdong.icredit.appsdk.retroapi.SdkApiService.class

@FormUrlEncoded
@POST("v1/admin/getAccessToken")
public abstract Observable<ApiResponse<TokenVO>> a(
	@Field("appId") String paramString1, 
	@Field("deviceId") String paramString2, 
	@Field("version") String paramString3, 
	@Field("deviceType") String paramString4, 
	@Field("os") String paramString5, 
	@Field("timestamp") long paramLong, 
	@Field("sign") String paramString6
	);
	

---


com.langdong.icredit.appsdk.retroapi.RetroBaseApi.class

public Observable<TokenVO> f()
  {
    long l1 = System.currentTimeMillis();
    String str = SdkHelper.a().c().a(new String[] { c, l1 + "", b });
    return e().a(a, c, "9.0.3", "android", "", l1, str).a(d());
  }
  
  
  ---
  
  
  appId 80c9ef0fb86369cd25f90af27ef53a9e
  deviceId V00IG/C/9fsDAFLGppYaSufx
  version 9.0.3
  deviceType android
  os 
  timestamp System.currentTimeMillis()
  sign SdkHelper.a().c().a(new String[] { c, l1 + "", b });
  
  
  ---
  
  sign:
  
  SdkHelper.a().c().a(deviceId, timestamp, b)
  
  ---
  
  b : Constants.f
  
##  com.android.icredit.AppApplication.class
  
  onCreate()
  
  Constants.f = localSecurityCipher.decryptString("437ujsOTfJqeBJwxtDebKUlsJIHeg2aD+qH+3Dur/iOIqrOdJciw8SB1WcAlVEvE", "00510944-78f5-4d1b-99a2-91c119a80edb");
   SdkHelper.a().c(Constants.f);
  
  
  
##  com.alibaba.wireless.security.jaq.SecurityCipher.class
  
  
    public String decryptString(String paramString1, String paramString2)
    throws JAQException
  {
    try
    {
      paramString1 = SecurityGuardManager.getInstance(this.a).getStaticDataEncryptComp().staticSafeDecrypt(16, paramString2, paramString1, "0335");
      return paramString1;
    }
    catch (SecException paramString1)
    {
      paramString1.printStackTrace();
      throw new JAQException(paramString1.getErrorCode());
    }
  }
  
  阿里云加密
  http://jaq.alibaba.com/
  
  
  python 调用java
  
  
  
  
  
  
  
  ---
  
  
  SdkHelper.a().c().a(deviceId, timestamp, b)
  
  
  
## com.android.icredit.utils.EncryptImpl.class
  
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
  
  
  
## com.alibaba.wireless.security.jaq.SecuritySignature.class

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
  
  
  