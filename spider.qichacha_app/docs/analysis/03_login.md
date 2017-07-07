com.langdong.icredit.appapi.retroapi.AppService.class


  @FormUrlEncoded
  @POST("v1/admin/login")
  public abstract Observable<ApiResponse<LoginResultVO>> a(
        @Header("Authorization") String paramString1, 
        @Field("loginType") String paramString2, 
        @Field("accountType") String paramString3, 
        @Field("account") String paramString4, 
        @Field("password") String paramString5, 
        @Field("identifyCode") String paramString6, 
        @Field("key") String paramString7, 
        @Field("token") String paramString8, 
        @Field("deviceToken") String paramString9, 
        @Field("timestamp") long paramLong, 
        @Field("sign") String paramString10
        );
  
  
---


  public Observable<LoginResultVO> a(TokenVO paramTokenVO, String paramString1, String paramString2, String paramString3, String paramString4, String paramString5, String paramString6, String paramString7, String paramString8)
  {
    if (d.equals("offline")) {
      return Observable.a(new ConnectException());
    }
    long l = System.currentTimeMillis();
    String str = SdkHelper.a().c().a(new String[] { c, l + "", b });
    paramTokenVO = paramTokenVO.getToken_type() + " " + paramTokenVO.getAccess_token();
    return a().a(paramTokenVO, paramString1, paramString2, paramString3, paramString4, paramString5, paramString6, paramString7, paramString8, l, str).a(d());
  }