com.langdong.icredit.appapi.retroapi.AppService.class

@GET("v1/admin/checkLoginType")
public abstract Observable<ApiResponse<LoginCheckVO>> a(
	@Header("Authorization") String paramString1, 
	@Query("telNo") String paramString2, 
	@Query("timestamp") long paramLong, 
	@Query("sign") String paramString3
	);
	

---


com.langdong.icredit.appapi.retroapiimpl.AppServiceImpl.class


  public Observable<LoginCheckVO> a(TokenVO paramTokenVO, String paramString)
  {
    if (d.equals("offline")) {
      return Observable.a(new ConnectException());
    }
    long l = System.currentTimeMillis();
    String str = SdkHelper.a().c().a(new String[] { c, l + "", b });
    paramTokenVO = paramTokenVO.getToken_type() + " " + paramTokenVO.getAccess_token();
    return a().a(paramTokenVO, paramString, l, str).a(d());
  }
  
  ---
  
  
  
  