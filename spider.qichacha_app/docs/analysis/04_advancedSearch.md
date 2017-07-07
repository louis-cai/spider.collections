
com.langdong.icredit.appsdk.retroapi.SdkApiService.class

  @GET("v1/base/advancedSearch")
  public abstract Observable<ApiResponse<SearchResultVO>> a(
        @Header("Authorization") String paramString1,
         @Query("searchKey") String paramString2, 
         @Query("searchIndex") String paramString3, 
         @Query("province") String paramString4, 
         @Query("cityCode") String paramString5, 
         @Query("pageIndex") int paramInt, 
         @Query("sortField") String paramString6, 
         @Query("isSortAsc") String paramString7, 
         @Query("startDateBegin") String paramString8, 
         @Query("startDateEnd") String paramString9, 
         @Query("registCapiBegin") String paramString10, 
         @Query("registCapiEnd") String paramString11, 
         @Query("industryCode") String paramString12, 
         @Query("subIndustryCode") String paramString13, 
         @Query("timestamp") long paramLong, 
         @Query("sign") String paramString14
         );
  
  
  ---
  
  com.langdong.icredit.appsdk.retroapiimpl.SdkApiServiceImpl.class
  
    public Observable<SearchResultVO> a(TokenVO paramTokenVO, String paramString1, String paramString2, int paramInt)
  {
    if (d.equals("offline")) {
      return Observable.a(new ConnectException());
    }
    long l = System.currentTimeMillis();
    String str = SdkHelper.a().c().a(new String[] { c, l + "", b });
    paramTokenVO = paramTokenVO.getToken_type() + " " + paramTokenVO.getAccess_token();
    return e().a(paramTokenVO, paramString1, paramString2, paramInt, "", "", l, str).a(d());
  }