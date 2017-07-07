单个用户,每天访问次数有限制

创建用户的时候,有个字段,加密了,validateStr	gVLY9w+zKjK41YG2VoELrg==

jni里加密的,

aes加密

需要分析c++代码

先放弃


 Object localObject = new HashMap();
      ((Map)localObject).put("mobile", EntPlusApplication.h().b);
      ((Map)localObject).put("pwd", h.a(String.format(EntPlusApplication.h().b + "{%s}", new Object[] { EntPlusApplication.h().b })));
      ((Map)localObject).put("validateStr", AESUtils.getImportantInfoByJNI(EntPlusApplication.h().b));
      localObject = new Request(ApiDefinition.OPT_FREE_MAN_MODE, (Map)localObject, LoginResponse.class);
      return (Request)localObject;