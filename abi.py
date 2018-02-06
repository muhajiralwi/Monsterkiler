# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE()
cl.login(token="Epm8gBtB3DhlfX4399P3.fFpQX1aq22TUtc5byTyeamW.dk+BBvv6RDtzgpOcvhdgrDxqKpaoWHaXos1OSXUKXOU=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EotOSE4zICePLK0sJGsGd.AJDuXFH4+90O8/AYgEE8pq.TjLVxG0wwwcTKmdJ3cPXPJOqaSm/4NYu/bPz9zUisbc=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EpthgTrLbXX2Vr88eGP09.oK4hZYO1ZAUBNRnucAEGMq.qzwCx+PpZ6r4NWFo4Eazhq2luRAio+SEDWzbecgIJxk=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Ep7dv1NSBUVSANlD0Y230.i+/lvhYna0zOvrSbImh+mW.xiFI0jw/ft/XbNj1rkZciicwvhv2Zf3FUMroDlLj2IM=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EpSeabmvTV0ObHU7cOyD9.MVAlv9AVfN+Ol5rPQpwx6q.+MLyyqz1sPJSh+sCpmr2OdgRuyAzdXlvoUVkw+LDeU8=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EpQJWhJssRORXrY4F07Td.FtUCrf+mUXfxvDgGrVw3Jq.j9vTPvNKs+iD5FGvxLvo2tWDxA5jl/+3LtollyKbgmc=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EpUE9nEwT3lvT7XpOMU78.Dlc+mioMBCJjO0imA6DY1W.blMaZD9HE+PQ2kDuxg1ckJlrWXM/mgdro0X3bS41gTk=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Ephi9TjHMc9LhFykWP827.5SWG5QIAij0V7qmpxo9tLW.diwil0FlpFnAkR9bm/JFBPZ7kdqUqziv5g3sJ7mKX1E=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EpgEMDbZ8lqTEv4ujWV1.8WCUBKBV9ufmrVoc5DD59Wq.Qq0azEjHetoNwkUURUOHfFPiuU/h48IDVp87McoWQF4=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EpOmTwjKMsN2SUp1oSUc.nYu24w1p0zkMliihwhwctZa.qKDShZpXfVcopXAXN0cJhU99ORiez7iw7NJ2kesCnpw=")
ki9.loginResult()

k1 = LINETCR.LINE()
k1.login(token="EpKzIdEBuJeVCaMTfeu4.oBs7zR8nk9DmcNtT8Ug3zXa.OVAa98sNAsi0/H+Izo/SYfnFTENwbwjG8Vet+g9EY2o=")
k1.loginResult()

k2 = LINETCR.LINE()
k2.login(token="Ep4jQZvZBNJQnyvIA3i0.YIBiEV8a4ivwmh+1GzS3XWa.iAuZDnhPdnjPMmo7ozULxxlN/hlZ9aYr05KHCNFQWb4=")
k2.loginResult()

k3 = LINETCR.LINE()
k3.login(token="EpXfr8X2MkIRUyRQYYGc.KF2h4YjKYR1X3IWVA0IRAVa.9ER8O7VYA0nZBxyxAKlJRdl77uAogB4M8NisC9orsxs=")
k3.loginResult()

k4 = LINETCR.LINE()
k4.login(token="EpG2LQLqTfbxzudOOlye.ZxRx04CXevF9tbXxaT9AwdG.jtdUTbkHNATLCbzGtKfHJGJYxe0YtlcFdZmv6IQ8xBg=")
k4.loginResult()

k5 = LINETCR.LINE()
k5.login(token="EpAwl6Xx1TwdFvkrzpPe.dxgbylMs4YF9kCn9JABNclG.cbLA3Aqyyf/Z0sQIQyNLrniS2jObmpvuBT1bYEI8vnE=")
k5.loginResult()

k6 = LINETCR.LINE()
k6.login(token="Ep9Sm9qUOoPiW811s27a.q9ZJa+vRR62SQpZQ9mzM4EG.OVfx7KAN1POehFF9KnBZPGAKvR0Do7XRpogvmGI0DbQ=")
k6.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

myhelpMessage ="""╔════════════════
╠-> TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅ ⱽ¹.⁰¹
╠═════════════════
╠-> Pᴏᴡᴇʀᴇᴅ:Bʏ Monster killer
╠═════════════════
╠->  ᴬᵖᵃᵏᵃʰ
╠->  ᴷᵃᵖᵃⁿ
╠->  ᴵᵈ
╠->  ᴹᵉ
╠->  ᴴᵃˡᵒ
╠->  ᴹᶦᵈ [ⁿᵃᵐᵉ]  
╠->  ˢᵉᵗˡᵃˢᵗᵖᵒᶦⁿᵗ ᵒⁿ\ᵒᶠᶠ 
╠->  ⱽᶦᵉʷˡᵃˢᵗˢᵉᵉⁿ
╠->  ᴸᵘʳᵏᶦⁿᵍ 
╠->  ᴿᵉˢᵘˡᵗ   
╠->  .ˢᵖᵉᵉᵈ 
╠->  ᴳᶦⁿᶠᵒ
╠->  ᵂᶦᵏᶦᵖᵉᵈᶦᵃ
╠->  ᶠᵇ [ᵗᵉˣᵗ]
╠->  ᴵⁿˢᵗᵃᵍʳᵃᵐ
╠->  ᴾʳᵒᶠᶦˡᵉᶦᵍ 
╠->  ᴹᵘˢᶦᶜ
╠->  /ᵐᵘˢᶦᵏ
╠->  /ᵐᵘˢʳᶦᵏ
╠->  ʸᵛᶦᵈᵉᵒ
╠->  ʸᵒᵘᵗᵘᵇᵉ
╠->  ᴰᵉᵗᵃᶦˡ @
╠->  ᴾᵖᵍʳᵒᵘᵖ
╠->  ᴾᵖ @
╠->  ᶜᵒᵛᵉʳ @
╠->  ʸᵒᵘᵗᵘᵇᵉᵐᵖ⁴
╠->  ʸᵗˢᵉᵃʳᶜʰ
╠->  ᴸᶦʳᶦᵏ
╠->  ʷᵉˡᶜᵒᵐᵉ
╠->  ᶠʳᶦᵉⁿᵈˡᶦˢᵗ
╠->  ᶠʳᶦᵉⁿᵈᶦⁿᶠᵒ
╠->  ᶠʳᶦᵉⁿᵈᵖᶦᶜᵗ
╠->  ᴹᵉᵐˡᶦˢᵗ
╠->  ᵀᵃᵍᵐᵉᵐ
╠═════════════════
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᶜᵒᵐᵐᵃⁿᵈ ᴳʳᵒᵘᵖˢ
╠═════════════════
╠⁻>  ˢᶦᵈᵉʳ ᵒⁿ
╠⁻>  ˢᶦᵈᵉʳ ᵒᶠᶠ
╠⁻>  ᴳˡᶦˢᵗ        
╠⁻>  ᶜᵃⁿᶜᵉˡ      
╠⁻>  ᴹᶦᵈ @         
╠⁻>  ᴵⁿᵛᶦᵗᵉ        
╠⁻>  ᴵⁿᵛᶦᵗᵉ:       
╠⁻>  ᵁⁿᵇᵃⁿ @   
╠⁻>  ᵂʰᶦᵗᵉˡᶦˢᵗ:   
╠⁻>  ᵁⁿᵇᵃⁿ:ᵒⁿ     
╠⁻>  ᴮˡᵃᶜᵏˡᶦˢᵗ @   
╠⁻>  ᴮˡᵃᶜᵏˡᶦˢᵗ:    
╠⁻>  ᴮˡᵃᶜᵏˡᶦˢᵗ  
╠⁻>  ᶜᵒⁿᵇᵃⁿ   
╠⁻>  ᶜˡᵉᵃʳ ᵇᵃⁿ     
╠⁻>  ᴸᶦⁿᵏ ᵒⁿ       
╠⁻>  ᴸᶦⁿᵏ ᵒᶠᶠ      
╠⁻>  ᴳᵘʳˡ          
╠⁻>  ᵁʳˡ           
╠⁻>  ᴳⁿ [ᵗᵉˣᵗ]        
╠⁻>  ᴮᵃⁿˡᶦˢᵗ       
╠⁻>  ᴰᵉᵗᵃᶦˡˢ ᵍʳᵘᵖ  
╠⁻>  ᴵⁿᵛᶦᵗᵉᵐᵉ:    
╠⁻>  ᴵⁿᶠᵒ ᵍʳᵘᵖ
╠⁻>  ᶜˡᵉᵃʳ ᵍʳᵘᵖ
╠⁻>  ˢᵉᵗˡᵃˢᵗᵖᵒᶦⁿᵗ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ⱽᶦᵉʷˡᵃˢᵗˢᵉᵉⁿ
╠⁻>  ᵀᵃᵍᵃˡˡ
╠⁻>  ʳᵉᵐᵒᵛᵉᶜʰᵃᵗ
╠⁻>  ᴿᵉᵇᵒᵒᵗ
╠═════════════════
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᶜᵒᵐᵐᵃⁿᵈ ᴷᶦᶜᶜᵏᵉʳ
╠═════════════════
╠⁻>  !ˢᵃˡᵃᵐ
╠⁻>  ᴺᵘᵏᵉ
╠⁻>  ᴷᶦᶜᵏᵃˡˡ
╠⁻>  ᴹᵃʸʰᵉᵐ
╠⁻>  ᴺᵏ @
╠⁻>  ᶠᵘᶜᵏ @        
╠⁻>  ᴷᶦᶜᵏ:
╠⁻>  ᴳʰᵒˢᵗ ᶦⁿ
╠⁻>  ᴳʰᵒˢᵗ ᵒᵘᵗ
╠⁻>  ᴾʳᵒ¹²³⁴⁵⁶ ᶦⁿ
╠⁻>  ᵖʳᵒ ¹²³⁴⁵⁶ ᵇʸᵉ
╠⁻>  ʸ
╠⁻>  ᴼ  
╠⁻>  ⁻
╠⁻>  ˢᵖᵃᵐᶜᵒⁿᵗᵃᶜᵗ @
╠⁻>  ˢᵖᵃᵐ ᶜʰᵃⁿᵍᵉ: 
╠⁻>  ᴳᶦᶠᵗ ²⁵ @  
╠⁻>  ˢᵖᵃᵐᵗᵃᵍ @   
╠════════════════
╠⁻> ˢᵉᶠᴮᵒᵗ Monster Killer<-=
╚════════════════
TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅
╔════════════════
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᶜᵒᵐᵃᵐᵃⁿᵈ ᴬᵈᵐᶦⁿ 
╠════════════════
╠⁻>  ˢᵉᵗ ᵃˡˡ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ᴮᵃᶜᵏᵘᵖ:ᵒⁿ/ᵒᶠᶠ
╠⁻>  ᵁᵖᵈᵃᵗᵉ ˢᵃᵐᵇᵘᵗᵃⁿ:
╠⁻>  ᴮᶜ:ᶜᵗ 
╠⁻>  ᴮᶜ:ᵍʳᵘᵖ
╠⁻>  ᴮˡᵒᶜᵏ @
╠⁻>  ᴮˡᵒᶜᵏˡᶦˢᵗ
╠⁻>  ˢᵖᵃᵐ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ᵁⁿᶦ
╠⁻>  ᴮᵒᵗ:ᶜᵗ        
╠⁻>  ᴮᵒᵗ:ᵍʳᵘᵖ      
╠⁻>  ᴬˡˡⁿᵃᵐᵉ:      
╠⁻>  ᴬˡˡᵇᶦᵒ:       
╠⁻>  ᴮᵒᵗ ˢᵖ  
╠⁻>  ᴿᵉᵇᵒᵒᵗ
╠⁻>  ᴿᵘⁿᵗᶦᵐᵉ 
╠⁻>  ᴿᵘⁿᵗᶦᵐᵉ¹     
╠⁻>  ˢᵖᵉᵉᵈ         
╠⁻>  ᴹʸᶜᵒᵖʸ @      
╠⁻>  ᴹʸᵇᵃᶜᵏᵘᵖ @  
╠⁻>  ᴾᵘʳᵍᵉ 
╠⁻>  ᴿᵉˢᵖᵒⁿᵏᶦᶜᵏ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ᴿᵉˢᵖᵒⁿ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ˢᶦᵐᶦˢᶦᵐᶦ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ˢᵃᵐᵇᵘᵗᵃⁿ ᵒⁿ/ᵒᶠᶠ
╠⁻>  ᴾˡᵃʸˢᵗᵒʳᵉ
╠⁻>  ᴿᵉᵐᵒᵛᵉ ᶜʰᵃᵗ
╠⁻>  ᴹᶦᵇᵒᵗ
╠⁻>  ᵂᵒʸ! @
╠════════════════
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᴴᵒˡˡᵒʷ ⱽᵉʳˢᶦᵒⁿ ⱽ¹.⁰¹
╚════════════════
 TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅
╔════════════════
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᶜᵒᵐᵐᵃⁿᵈ ˢᵉᵗ
╠════════════════      
╠⁻>  [ᴸᶦᵏᵉ:ᵒⁿ/ᵒᶠᶠ]     
╠⁻>  [ᴬᵈᵈ ᵒⁿ/ᵒᶠᶠ] 	 
╠⁻>  [ᴬᵘᵗᵒ ʲᵒᶦⁿ ᵒⁿ/ᵒᶠᶠ] 	   
╠⁻>  [ᶜᵒⁿᵗᵃᶜᵗ ᵒⁿ/ᵒᶠᶠ] 	
╠⁻>  [ᴸᵉᵃᵛᵉ ᵒⁿ/ᵒᶠᶠ]  
╠⁻>  [ˢʰᵃʳᵉ ᵒⁿ/ᵒᶠᶠ]           
╠⁻>  [ᴬᵈᵈ ᵒⁿ/ᵒᶠᶠ] 		   
╠⁻>  [ᴶᵃᵐ ᵒⁿ/ᵒᶠᶠ]			   
╠⁻>  [ᴶᵃᵐ ˢᵃʸ:]			   
╠⁻>  [ᶜᵒᵐ ᵒⁿ/ᵒᶠᶠ]	
╠⁻>  [ᴹᵉˢˢᵃᵍᵉ ˢᵉᵗ:]	
╠⁻>  [ᶜᵒᵐᵐᵉⁿᵗ ˢᵉᵗ:]	
╠⁻>  [ᴾᵉˢᵃⁿ ᵃᵈᵈ:]
╠⁻>  [ˢᵉᵗ ᵃˡˡ ᵒⁿ]
╠═════════════════ 
╠⁻> ˢᵉˡᶠᴮᵒᵗ ᶜᵒᵐᵐᵃⁿᵈ ᴾʳᵒᵗᵉᶜᵗ
╠═════════════════       
╠⁻> [ᴾᵃⁿᶦᶜᵏ:ᵒⁿ/ᵒᶠᶠ]      
╠⁻> [ᴾʳᵒᵗᵉᶜᵗ ᵒⁿ]			   
╠⁻> [Qʳᵖʳᵒᵗᵉᶜᵗ ᵒⁿ/ᵒᶠᶠ]			   
╠⁻> [ᴵⁿᵛᶦᵗᵉᵖʳᵒᵗᵉᶜᵗ ᵒⁿ/ᵒᶠᶠ]			   
╠⁻> [ᶜᵃⁿᶜᵉˡᵖʳᵒᵗᵉᶜᵗ ᵒⁿ/ᵒᶠᶠ]		   
╠⁻> [ᴿᵉˢᵖᵒⁿ ᵒⁿ/ᵒᶠᶠ]
╠⁻> [ᴿᵉˢᵖᵒⁿᵏᶦᶜᵏ ᵒⁿ/ᵒᶠᶠ] 
╠⁻> [ˢᵃᵐᵇᵘᵗᵃⁿ ᵒⁿ/ᵒᶠᶠ]
╠⁻> [ᴮᵃᶜᵏᵘᵖ ᵒⁿ/ᵒᶠᶠ]
╠═════════════════
╠⁻> TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅
╠═════════════════
╠⁻>👆🎌🎌🎌🎌🎌🎌🎌☝
╠═════════════════
╠⁻> TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅
╚═════════════════

"""
helo=""

KAC=[cl]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
k1mid = k1.getProfile().mid
k2mid = k2.getProfile().mid
k3mid = k3.getProfile().mid
k4mid = k4.getProfile().mid
k5mid = k5.getProfile().mid
k6mid = k6.getProfile().mid
#k7mid = k7.getProfile().mid
#k8mid = k8.getProfile().mid
#k9mid = k9.getProfile().mid
#w1mid = w1.getProfile().mid
#w2mid = w2.getProfile().mid
#w3mid = w3.getProfile().mid
#w4mid = w4.getProfile().mid
#w5mid = w5.getProfile().mid
#w6mid = w6.getProfile().mid
#w7mid = w7.getProfile().mid
#w8mid = w8.getProfile().mid
#w9mid = w9.getProfile().mid
#l1mid = l1.getProfile().mid
#l2mid = l2.getProfile().mid
#l3mid = l3.getProfile().mid
#l4mid = l4.getProfile().mid
#l5mid = l5.getProfile().mid

admin = []
targets = []
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,"u15fab1d40436dadb930b9058b5810033"]
creator = "u15fab1d40436dadb930b9058b5810033"
admsa = "u15fab1d40436dadb930b9058b5810033"
admin = "u15fab1d40436dadb930b9058b5810033"
whitelist=[""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'AutoJoinCancel':True,
    'Admin':True,
    'Members':1,
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Hayo ketauan nge add..... ternyata baper...",
    "lang":"JP",
    "comment":"Auto Like By ✟rozikeane✟一�:緑\n\nCreator : Http://line.me/ti/p/~rozikeane",
    "commentOn":False,
    "likeOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "detectMention":True,
    "kickMention":False,
    "Backup":False,
    "Sider":{},
    "sticker":False,
    "Sambutan":True,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
 
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }      
    
setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki6.getProfile()
backup = ki6.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki7.getProfile()
backup = ki7.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def removeAllMessages(self, lastMessageId):
        return self.Talk.client.removeAllMessages(0, lastMessageId)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs) 
    
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi    
    
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
         
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)                                      
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u923fca3dc907e047572ad25c24f1d29b":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")                                                      
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    balas = [cName + "\n Iɴɪ Pᴇɴᴀᴍᴘᴀᴋᴀɴ Mᴀᴋʜʟᴜᴋ Jᴏɴᴇs \nYᴀɴɢ sᴜᴋᴀ Nɢᴇᴛᴀɢ ɢᴡ!! ",cName + "\nHᴀʟᴏ Fᴀɴs Bᴇʀᴀᴛ Gᴡ!! \nAᴅᴀ Pᴇʀʟᴜ ᴀᴘᴀ Tᴀɢ Gᴡ..",cName + "\nᴬᵈᵃ ᴬᵖᵃ ᵀᵃᵍ ᴳʷ>>! \nᴹᵃᵘ ᴹⁿᵗᵃ ᵀᵃⁿᵈᵃ ᵀᵃⁿᵍᵃⁿ ᴳʷ!!!",cName + "\nHᴀᴅɪʀʀʀʀʀ Sᴇʟᴀʟᴜ \nAᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ",cName + "\nᴶᵃⁿᵍᵃⁿ ᵀᵃᵍ,, ᴷᵃⁿᵍᵉⁿ ᴾᶜ ˡᵃⁿᵍˢᵘⁿᵍ ᴬʲᵃ",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nPᴇʀɢɪ sᴀɴᴀ ᴊᴀᴜʜ ᴊᴀᴜʜ \nHᴜs Hᴜs Hᴜs"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = "[Auto Respond] \n" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to,path)
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '10183488',
                                    'STKPKGID': '1251076',
                                    'STKVER': '1'}
                                    #'STKVER': '1'}
                                  cl.sendMessage(msg) 
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '10183488',
                                    'STKPKGID': '1251076',
                                    'STKVER': '1'}
                                    #'STKVER': '1'}
                                  
                                  cl.sendMessage(msg)                                
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '10183488',
                                    'STKPKGID': '1251076',
                                    'STKVER':'1'}
                                  
                                  cl.sendMessage(msg)                                
                                  
                                  break                                                             
            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + " Kenapa Tag saya?,  " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., ", "Tersummon -_-, "]
                     ret_ = "[**Auto Respond**]\n " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break  
                                            
        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "☸ Sticker Check ☸\n\n☑ STKID : %s\n☑ STKPKGID : %s\n☑ STKVER : %s\n☸ Link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass                    

       
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"sᴜᴋsᴇs ᴍᴇɴɢɪɴᴠɪᴛᴇ ɢᴇᴍʙᴇʟ ɪɴɪ \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'aku':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,myhelpMessage)
                else:
                    cl.sendText(msg.to,myhelpMessage)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                k6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                #k7.sendMessage(msg)
                #msg.contentType = 13
               # msg.contentMetadata = {'mid': k8mid}
               # k8.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': k9mid}
               # k9.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w1mid}
               # w1.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w2mid}
               # w2.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w3mid}
               # w3.sendMessage(msg) 
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w4mid}
               # w4.sendMessage(msg) 
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w5mid}
               # w5.sendMessage(msg) 
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w6mid}
               # w6.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w7mid}
               # w7.sendMessage(msg) 
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w8mid}
               # w8.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': w9mid}
               # w9.sendMessage(msg)
               # msg.contentType = 13
               # msg.contentMetadata = {'mid': l1mid}
              #  l1.sendMessage(msg)
              #  msg.contentType = 13
              #  msg.contentMetadata = {'mid': l2mid}
              #  l2.sendMessage(msg)
              #  msg.contentType = 13
              #  msg.contentMetadata = {'mid': l3mid}
              #  l3.sendMessage(msg)
              #  msg.contentType = 13
              #  msg.contentMetadata = {'mid': l4mid}
              #  l4.sendMessage(msg)
              #  msg.contentType = 13
              #  msg.contentMetadata = {'mid': l5mid}
              #  l5.sendMessage(msg)
            elif "Pro1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Pro2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Pro3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Pro4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Pro5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "Pro6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "Pro7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "Pro8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
      #      elif "Pro9" == msg.text:
          #      msg.contentType = 13
           #     msg.contentMetadata = {'mid': ki9mid}
         #       ki9.sendMessage(msg)
        #    elif "Pro10" == msg.text:
          #      msg.contentType = 13
          #      msg.contentMetadata = {'mid': k1mid}
             #   k1.sendMessage(msg)
          #  elif "Pro11" == msg.text:
           #     msg.contentType = 13
             #   msg.contentMetadata = {'mid': k2mid}
              #  k2.sendMessage(msg)
           # elif "Pro12" == msg.text:
              #  msg.contentType = 13
             #   msg.contentMetadata = {'mid': k3mid}
              #  k3.sendMessage(msg)
           # elif "Pro13" == msg.text:
               # msg.contentType = 13
              #  msg.contentMetadata = {'mid': k4mid}
          #      k4.sendMessage(msg)
          #  elif "Pro14" == msg.text:
            #    msg.contentType = 13
             #   msg.contentMetadata = {'mid': k5mid}
              #  k5.sendMessage(msg)
           # elif "Pro15" == msg.text:
          #      msg.contentType = 13
            #    msg.contentMetadata = {'mid': k6mid}
              #  k6.sendMessage(msg)
          #  elif "Pro16" == msg.text:
             #   msg.contentType = 13
             #   msg.contentMetadata = {'mid': k7mid}
             #   k7.sendMessage(msg)
           # elif "Pro17" == msg.text:
            #    msg.contentType = 13
            #    msg.contentMetadata = {'mid': k8mid}
              #  k8.sendMessage(msg)
           # elif "Pro18" == msg.text:
            #    msg.contentType = 13
             #   msg.contentMetadata = {'mid': k9mid}
             #   k9.sendMessage(msg)
           # elif "Pro19" == msg.text:
              #  msg.contentType = 13
              #  msg.contentMetadata = {'mid': w1mid}
               # w1.sendMessage(msg)
           # elif "Pro20" == msg.text:
              #  msg.contentType = 13
             #   msg.contentMetadata = {'mid': w2mid}
             #   w2.sendMessage(msg)
          #  elif "Pro21" == msg.text:
              #  msg.contentType = 13
                #msg.contentMetadata = {'mid': w3mid}
               # w3.sendMessage(msg) 
           # elif "Pro22" == msg.text:
           #     msg.contentType = 13
           #     msg.contentMetadata = {'mid': w4mid}
           #     w4.sendMessage(msg) 
            #elif "Pro23" == msg.text:
             #   msg.contentType = 13
              #  msg.contentMetadata = {'mid': w5mid}
              #  w5.sendMessage(msg) 
            #elif "Pro24" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': w6mid}
                #w6.sendMessage(msg)
            #elif "Pro25" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': w7mid}
                #w7.sendMessage(msg) 
            #elif "Pro26" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': w8mid}
                #w8.sendMessage(msg)
            #elif "Pro27" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': w9mid}
                #w9.sendMessage(msg)
            #elif "Pro28" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': l1mid}
                #l1.sendMessage(msg)
            #elif "Pro29" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': l2mid}
                #l2.sendMessage(msg)
            #elif "Pro30" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': l3mid}
                #l3.sendMessage(msg)
            #elif "Pro31" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': l4mid}
                #l4.sendMessage(msg)
            #elif "Pro32" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': l5mid}
                #l5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Pro1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Pro2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Pro3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Pro4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Pro5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Pro6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "Pro7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "Pro8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
#            elif "Pro9 mid" == msg.text:
#                ki9.sendText(msg.to,ki9mid)
#            elif "Pro10 mid" == msg.text:
#                k1.sendText(msg.to,k1mid)
#            elif "Pro11 mid" == msg.text:
#                k2.sendText(msg.to,k2mid)
#            elif "Pro12 mid" == msg.text:
#                k3.sendText(msg.to,k3mid)
#            elif "Pro13 mid" == msg.text:
#                k4.sendText(msg.to,k4mid)
#            elif "Pro14 mid" == msg.text:
#                k5.sendText(msg.to,k5mid)
#            elif "Pro15 mid" == msg.text:
#                k6.sendText(msg.to,k6mid)
#            elif "Pro16 mid" == msg.text:
#                k7.sendText(msg.to,k7mid)
#            elif "Pro17 mid" == msg.text:
#                k8.sendText(msg.to,k8mid)
#            elif "Pro18 mid" == msg.text:
#                k9.sendText(msg.to,k9mid)
#            elif "Pro19 mid" == msg.text:
#                w1.sendText(msg.to,w1mid)
#            elif "Pro20 mid" == msg.text:
#                w2.sendText(msg.to,w2mid)
#            elif "Pro21 mid" == msg.text:
#                w3.sendText(msg.to,w3mid)
#            elif "Pro22 mid" == msg.text:
#                w4.sendText(msg.to,w4mid)
#            elif "Pro23 mid" == msg.text:
#                w5.sendText(msg.to,w5mid)
#            elif "Pro24 mid" == msg.text:
#                w6.sendText(msg.to,w6mid)
#            elif "Pro25 mid" == msg.text:
#                w7.sendText(msg.to,w7mid)
#            elif "Pro26 mid" == msg.text:
#                w8.sendText(msg.to,w8mid)
#            elif "Pro27 mid" == msg.text:
#                w9.sendText(msg.to,w9mid)
#            elif "Pro28 mid" == msg.text:
#                l1.sendText(msg.to,l1mid)
#            elif "Pro29 mid" == msg.text:
#                l2.sendText(msg.to,l2mid)
#            elif "Pro30 mid" == msg.text:
#                l3.sendText(msg.to,l3mid)
#            elif "Pro31 mid" == msg.text:
#                l4.sendText(msg.to,l4mid)
#            elif "Pro32 mid" == msg.text:
#                l5.sendText(msg.to,l5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                #k1.sendText(msg.to,k1mid)
                #k2.sendText(msg.to,k2mid)
                #k3.sendText(msg.to,k3mid)
                #k4.sendText(msg.to,k4mid)
                #k5.sendText(msg.to,k5mid)
                #k6.sendText(msg.to,k6mid)
                #k7.sendText(msg.to,k7mid)
                #k8.sendText(msg.to,k8mid)
                #k9.sendText(msg.to,k9mid)
                #w1.sendText(msg.to,w1mid)
                #w2.sendText(msg.to,w2mid)
                #w3.sendText(msg.to,w3mid)
                #w4.sendText(msg.to,w4mid)
                #w5.sendText(msg.to,w5mid)
                #w6.sendText(msg.to,w6mid)
                #w7.sendText(msg.to,w7mid)
                #w8.sendText(msg.to,w8mid)
                #w9.sendText(msg.to,w9mid)
                #l1.sendText(msg.to,l1mid)
                #l2.sendText(msg.to,l2mid)
                #l3.sendText(msg.to,l3mid)
                #l4.sendText(msg.to,l4mid)
                #l5.sendText(msg.to,l5mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
#                    ki9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k1.getProfile()
#                    profile.displayName = string
#                    k1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k2.getProfile()
#                    profile.displayName = string
#                    k2.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k3.getProfile()
#                    profile.displayName = string
#                    k3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k4.getProfile()
#                    profile.displayName = string
#                    k4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k5.getProfile()
#                    profile.displayName = string
#                    k5.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k6.getProfile()
#                    profile.displayName = string
#                    k6.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k7.getProfile()
#                    profile.displayName = string
#                    k7.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k8.getProfile()
#                    profile.displayName = string
#                    k8.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k9.getProfile()
#                    profile.displayName = string
#                    k9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w1.getProfile()
#                    profile.displayName = string
#                    w1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w2.getProfile()
#                    profile.displayName = string
#                    w2.updateProfile(profile)
#               if len(string.decode('utf-8')) <= 20:
#                    profile = w3.getProfile()
#                    profile.displayName = string
#                    w3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w4.getProfile()
#                    profile.displayName = string
#                    w4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w5.getProfile()
#                    profile.displayName = string
#                    w5.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w6.getProfile()
#                    profile.displayName = string
#                    w6.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w7.getProfile()
#                    profile.displayName = string
#                    w7.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w8.getProfile()
#                    profile.displayName = string
#                    w8.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w9.getProfile()
#                    profile.displayName = string
#                    w9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l1.getProfile()
#                    profile.displayName = string
#                    l1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l2.getProfile()
#                    profile.displayName = string
#                    l2.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l3.getProfile()
#                    profile.displayName = string
#                    l3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l4.getProfile()
#                    profile.displayName = string
#                    l4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l5.getProfile()
#                    profile.displayName = string
#                    l5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)  
#---------------------------------------------------------
            elif msg.text in ["Meong"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)              
#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁??􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6pro: " in msg.text:
                string = msg.text.replace("6pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
 #--------------------------------------------------------
            elif "7pro: " in msg.text:
                string = msg.text.replace("7pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8pro: " in msg.text:
                string = msg.text.replace("8pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                              
#--------------------------------------------------------
            elif msg.text in ["Joinl on","Autojoinl on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    nadya.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    nadya.sendText(msg.to,"Khusus Alvian")

            elif msg.text in ["Join1 off","Autojoin1 off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    nadya.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    nadya.sendText(msg.to,"Khusus Alvian")
#--------------------------------------------------------
            elif msg.text.lower() == 'runtime':
                cl.sendText(msg.to,"「ᴾˡᵉᵃˢᵉ ʷᵃᶦᵗ..」\nᵀʸᵖᵉ  :ᴸᵒᵃᵈᶦⁿᵍ...\ⁿˢᵗᵃᵗᵘˢ : ᴸᵒᵃᵈᶦⁿᵍ...")
                eltime = time.time() - mulai
                van = "ᵀʸᵖᵉ : ˢᵉˡᶠᴮᵒᵗ ˢᵉᵈᵃⁿᵍ ᴮᵉʳʲᵃˡᵃⁿ \nˢᵗᵃᵗᵘˢ : ᴬᵏᵗᶦᶠ \nᴹʸˢᵉˡᵇᵒᵗ ˢᵘᵈᵃʰ ᵇᵉʳʲᵃˡᵃⁿ ˢᵉˡᵃᵐᵃ"+waktu(eltime)
                cl.sendText(msg.to,van)
            elif msg.text.lower() == 'runtime1':
                eltime = time.time() - mulai
                van = "ᴮᵒᵗ ʰᵃˢ ᵇᵉᵉⁿ ᵃᶜᵗᶦᵛᵉ "+waktu(eltime)
                cl.sendText(msg.to,van)                
#--------------------------------------------------------
            elif "Update sambutan:" in msg.text:
              #if msg.from_ in admin + owner + creator:
                wait["Sambutan"] = msg.text.replace("Update sambutan:","")
                cl.sendText(msg.to,"ˢᵃᵐᵇᵘᵗᵃⁿ ᴬᵏᵗᶦᵛᵉ ᶜʰᵃⁿᵍᵉᵈ"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              #if msg.from_ in admin + creator + owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ʸᵒᵘʳ ᴮᵒᵗ ᴹᵉˢˢᵃᵍᵉ\n\n" + wait["Sambutan"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["Sambutan"])
#--------------------------------------------------------
            elif msg.text == "Sp":
            	    start = time.time()
            	    print("Speed") 
                    cl.sendText(msg.to,"「ᴸᵒᵃᵈᶦᵃⁿᵍ.....」\nᵀᵉˢᵀᵉᵈ ˢᵖᵉᵈ ˢᵉˡᶠᵇᵒᵗ")
                    for i in range(3000):
                        1+1
                    elsp = time.time() - start
                    cl.sendText(msg.to,"%s/ᴰᵉᵗᶦᵏ" % (elsp))    
                
            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u923fca3dc907e047572ad25c24f1d29b'}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")                
#--------------------------------------------------------
            elif "Spam change:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam change:","")
                cl.sendText(msg.to,"spam changed")
#--------------------------------------------------------
            elif "Admin add @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                gs = ki3.getGroup(msg.to)
                gs = ki4.getGroup(msg.to)
                gs = ki5.getGroup(msg.to)
                gs = ki6.getGroup(msg.to)
                gs = ki7.getGroup(msg.to)
                gs = ki8getGroup(msg.to)
                #gs = ko.getGroup(msg.to)
                #gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                gs = ki3.getGroup(msg.to)
                gs = ki4.getGroup(msg.to)
                gs = ki5.getGroup(msg.to)
                gs = ki6.getGroup(msg.to)
                gs = ki7.getGroup(msg.to)
                gs = ki8.getGroup(msg.to)
                #gs = ko.getGroup(msg.to)
               # gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||List Admin Selfbot Hollow||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#--------------------------------------------------------
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵃᶜᵗᶦᵛᵉ"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵉⁿᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵉⁿᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵘⁿᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵈᶦˢᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵘⁿᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵈᶦˢᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
#-------------------------------------------------------- 
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = ki2.getGroup(msg.to)
                  gs = ki3.getGroup(msg.to)
                  gs = ki4.getGroup(msg.to)
                  gs = ki5.getGroup(msg.to)
                  gs = ki6.getGroup(msg.to)
                  gs = ki7.getGroup(msg.to)
                  gs = ki8.getGroup(msg.to)
                  #gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                        ki3.findAndAddContactsByMid(target)
                        ki4.findAndAddContactsByMid(target)
                        ki5.findAndAddContactsByMid(target)
                        ki6.findAndAddContactsByMid(target)
                        ki7.findAndAddContactsByMid(target)
                        ki8.findAndAddContactsByMid(target)
                        #ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")                       
#--------------------------------------------------------
            elif "Mayhem" in msg.text:
                if msg.toType == 2:
                    print "Cleanse is going."
                    _name = msg.text.replace("Mayhem ","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴀᴋᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    cl.sendText(msg.to,"sᴀʏ ɢᴏᴏᴅ ʙʏᴇ ᴛᴏ ᴍᴇ")
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                                cl.sendText(msg.to,"ɢʀᴏᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴇʀsɪʜᴋᴀɴ")
                            except:
                                cl.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
#-------------------------------------------------------
            elif msg.text in ["Purge"]:
              if msg.from_ in admin :
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"group purge")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#--------------------------------------------------------
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᶜᵉᵏ ᴼⁿ ˢᶦᵈᵉʳ...")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ᶜᵉᵏ ˢᶦᵈᵉʳ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    cl.sendText(msg.to, "ᴮᵉˡᵘᵐ ᴰᶦˢᵉᵗ ᴰᵘᵈᵘˡ")                            
#--------------------------------------------------------
            elif "setpoint on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"ˢᵉᵗᵖᵒᶦⁿᵗ ᵃˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "setpoint off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"ˢᵉᵗ ʳᵉᵃᵈᶦⁿᵍ ᵖᵒᶦⁿᵗ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ᴰᵉˡᵉᵗᵉᵈ ᴿᵉᵃᵈʸⁿᵍ ᴾᵒᶦⁿᵗ:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "viewlastseen" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "ᴸᵘʳᵏᶦⁿᵍ ᴴᵃˢ ᴺᵒᵗ ᴮᵉⁿ ˢᵉᵗ.")
#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Simi mode Off")
                
            #elif msg.text in ["Autoread on","Read:on"]:
                #wait['alwayRead'] = True
                #cl.sendText(msg.to,"Auto read On")
                
            #elif msg.text in ["Autoread off","Read:off"]:
                #wait['alwayRead'] = False
                #cl.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴿᵉˢᵖᵒⁿ ᵀᵃᵍ ᴵⁿ ᴬᶜᵗᶦᵛᵉ")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴿᵉˢᵖᵒⁿ ᵀᵃᵍ ᴰᶦˢᵃᵇˡᵉ")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴷᶦᶜᵏ ᵀᵃᵍ ᴵⁿ ᴬᶜᵗᶦᵛᵉ")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴷᶦᶜᵏ ᵀᵃᵍ ᴰᶦˢᵃᵇˡᵉ")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif "Tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Para Jones"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
#==============================================================================#
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "ytsearch " in msg.text:
                    query = msg.text.replace("ytsearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "LinkNya: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollowerNya : "+followerIG+"\nFollowingNya : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "********************\n"
                    details = "\n********************="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#=============================================================================#
            elif "tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " ᴾᵃʳᵃ ᴶᵒⁿᵉˢ ᴬᵏᵘᵈ"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)                
#==============================================================================#
            elif msg.text in ["Set all on"]:
		if msg.from_ in admsa:
                    wait["protect"] = True
                    wait["cancelprotect"] = True
                    wait["inviteprotect"] = True
                    wait["linkprotect"] = True
                    wait["Backup"] = True
                    #wait["Contact"] = True
                    wait["Sambutan"] = True
                    cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ ˢᵉᵗᵗᶦⁿᵍ ᴵⁿ ᴬᶜᵗᶦᵛᵉ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")

            elif msg.text in ["Set all off"]:
		if msg.from_ in admsa:
                    wait["protect"] = False
                    wait["cancelprotect"] = False
                    wait["inviteprotect"] = False
                    wait["linkprotect"] = False
                    wait["Backup"] = False
                    #wait["Contact"] = False
                    wait["Sambutan"] = False
                    cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ ˢᵉᵗᵗᶦⁿᵍ ᴰᶦˢᵃᵇˡᵉ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")
#==============================================================================#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        ki8.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        ki8.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
#==============================================================================#
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                    else:
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'set':
                md = ""
                if wait["Backup"] == True: md+="☞ Bᴀᴄᴋᴜᴘ → ✔\n"
                else: md+="☞ Bᴀᴄᴋᴜᴘ → ❌\n"
                if wait["kickMention"] == True: md+="☞ Aᴜᴛᴏ Rᴇsᴘᴏɴ Kɪᴄᴋ → ✔\n"
                else: md+="☞ Aᴜᴛᴏ Rᴇsᴘᴏɴ Kɪᴄᴋ → ❌\n"
                if wait["detectMention"] == True: md+="☞ Aᴜᴛᴏ Rᴇsᴘᴏɴ → ✔\n"
                else: md+="☞ Aᴜᴛᴏ Rᴇsᴘᴏɴ → ❌\n"
                if wait["Sambutan"] == True: md+="☞ Sᴀᴍʙᴜᴛᴀɴ → ✔\n"
                else: md+="☞ Sᴀᴍʙᴜᴛᴀɴ → ❌\n"
                if wait["contact"] == True: md+="☞ Cᴏɴᴛᴀᴄᴛ → ✔\n"
                else: md+="☞ Cᴏɴᴛᴀᴄᴛ → ❌\n"
                if wait["autoJoin"] == True: md+="☞ Aᴜᴛᴏ Jᴏɪɴ → ✔\n"
                else: md+="☞ Aᴜᴛᴏ Jᴏɪɴ → ❌\n"
                if wait["autoCancel"]["on"] == True:md+="☞ Gʀᴏᴜᴘ Cᴀɴᴄᴇʟ: " + str(wait["autoCancel"]["members"]) + " → ✔\n"
                else: md+="☞ Gʀᴏᴜᴘ Cᴀɴᴄᴇʟ → ❌\n"
                if wait["leaveRoom"] == True: md+="☞ Aᴜᴛᴏ Lᴇᴀᴠᴇ → ✔\n"
                else: md+="☞ Aᴜᴛᴏ Lᴇᴀᴠᴇ → ❌\n"
                if wait["timeline"] == True: md+="☞ Sʜᴀʀᴇ → ✔\n"
                else:md+="☞ Sʜᴀʀᴇ → ❌\n"
                if wait["autoAdd"] == True: md+="☞ Aᴜᴛᴏ Aᴅᴅ → ✔\n"
                else:md+="☞ Aᴜᴛᴏ Aᴅᴅ → ❌\n"
                if wait["commentOn"] == True: md+="☞ Aᴜᴛᴏ Cᴏᴍᴇɴᴛ → ✔\n"
                else:md+="☞ Aᴜᴛᴏ Cᴏᴍᴇɴᴛ → ❌\n"
                if wait["protect"] == True: md+="☞ Protect → ✔\n"
                else:md+="☞ Pʀᴏᴛᴇᴄᴛ → ❌\n"
                if wait["linkprotect"] == True: md+="☞ Uʀʟ Pʀᴏᴛᴇᴄᴛ → ✔\n"
                else:md+="☞ Uʀʟ Pʀᴏᴛᴇᴄᴛ → ❌\n"
                if wait["inviteprotect"] == True: md+="☞ Dᴇɴʏ ɪɴᴠɪᴛᴇ → ✔\n"
                else:md+="☞ Dᴇɴʏ ɪɴᴠɪᴛᴇ → ❌\n"
                if wait["cancelprotect"] == True: md+="☞ Cᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ → ✔\n"
                else:md+="☞ Cᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ → ❌\n"
                if wait["likeOn"] == True: md+="☞ Aᴜᴛᴏ Lɪᴋᴇ → ✔\n"
                else:md+="☞ Aᴜᴛᴏ Lɪᴋᴇ → ❌\n" 
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text == "Lurking":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Set reading point:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Result":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n [☸]➦Powered By: Alin々•┅─────" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")

#-----------------------[Add Staff Section]------------------------								
#-----------------------------------------------------------   

#-----------------------------------------------------------

#----------------------------------------------------------------
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Checking Sider Already Active")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ᶜʰᵉᶜᵏᶦⁿᵍ ˢᶦᵈᵉʳ ᴬˡʳᵉᵃᵈʸ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    cl.sendText(msg.to, "ᴮᵉˡᵘᵐ ᴰᶦ ˢᵉᵗ ⱽᵉᵏᵒᵏ ")           
#-----------------------------------------------------------
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#-----------------------------------------------------------
            elif "tagmem" == msg.text:
		    group = cl.getGroup(msg.to)
		    mem = [contact.mid for contact in group.members]
		    for mm in mem:
		        xname = cl.getContact(mm).displayName
		        xlen = str(len(xname)+1)
		        msg.contentType = 0
		        msg.text = "@"+xname+" "
		        msg.contentMetadata = {'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		        try:
		            cl.sendMessage(msg)
		        except Exception as e:
			    print str(e)


            elif msg.text in ["Tagall","Tag all"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                      #cl.sendText(receiver, "Members :"+str(jml))
                  except Exception as error:
                      print error                        
#-----------------------------------------------------------)
            elif 'gn ' in msg.text.lower():
                if msg.toType == 2:
                    wildan = cl.getGroup(msg.to)
                    wildan.name = msg.text.replace("gn ","")
                    cl.updateGroup(wildan)
                    cl.sendText(msg.to,"Nᴀᴍᴇ Gʀᴏᴜᴘs Iᴛs Cʜᴀɴɢᴇᴅ 😀")
#----------------------ADMIN COMMAND------------------------------#

            elif ("Fuck " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            #cl.sendText(msg.to,"Fᴜᴄᴋ Fᴏʀ Yᴏᴜ Iᴅɪᴏᴛs"
                        except:
                            cl.sendText(msg.to,"Error")
                    
            elif "Halo" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

            elif "Kickall" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Kickall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       gs = ki.getGroup(msg.to)
                       gs = ki2.getGroup(msg.to)
                       gs = ki3.getGroup(msg.to)
                       gs = ki4.getGroup(msg.to)
                       gs = ki5.getGroup(msg.to)
                       gs = ki6.getGroup(msg.to)
                       gs = ki7.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)

            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")

            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Mysteal @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Mysteal @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki2.cloneContactProfile(target)
                                    ki3.cloneContactProfile(target)
                                    ki4.cloneContactProfile(target)
                                    ki5.cloneContactProfile(target)
                                    ki6.cloneContactProfile(target)
                                    ki7.cloneContactProfile(target)
                                    ki8.cloneContactProfile(target)
                                    #ki9.cloneContactProfile(target)
                                    #k1.cloneContactProfile(target)
                                    #k2.cloneContactProfile(target)
                                    #k3.cloneContactProfile(target)
                                    #k4.cloneContactProfile(target)
                                    #k5.cloneContactProfile(target)
                                    #k6.cloneContactProfile(target)
                                    #k7.cloneContactProfile(target)
                                    #k8.cloneContactProfile(target)
                                    #k9.cloneContactProfile(target)
                                    #w1.cloneContactProfile(target)
                                    #w2.cloneContactProfile(target)
                                    #w3.cloneContactProfile(target)
                                    #w4.cloneContactProfile(target)
                                    #w5.cloneContactProfile(target)
                                    #w6.cloneContactProfile(target)
                                    #w7.cloneContactProfile(target)
                                    #w8.cloneContactProfile(target)
                                    #w9.cloneContactProfile(target)
                                    #l1.cloneContactProfile(target)
                                    #l2.cloneContactProfile(target)
                                    #l3.cloneContactProfile(target)
                                    #l4.cloneContactProfile(target)
                                    #k5.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki5.updateDisplayPicture(backup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki6.updateDisplayPicture(backup.pictureStatus)
                    ki6.updateProfile(backup)
                    ki7.updateDisplayPicture(backup.pictureStatus)
                    ki7.updateProfile(backup)
                    ki8.updateDisplayPicture(backup.pictureStatus)
                    ki8.updateProfile(backup)
                    #ki9.updateDisplayPicture(backup.pictureStatus)
                    #ki9.updateProfile(backup)
                    #k1.updateDisplayPicture(backup.pictureStatus)
                    #k1.updateProfile(backup)
                    #k2.updateDisplayPicture(backup.pictureStatus)
                    #k2.updateProfile(backup)
                    #k3.updateDisplayPicture(backup.pictureStatus)
                    #k3.updateProfile(backup)
                    #k4.updateDisplayPicture(backup.pictureStatus)
                    #k4.updateProfile(backup)
                    #k5.updateDisplayPicture(backup.pictureStatus)
                    #k5.updateProfile(backup)
                    #k6.updateDisplayPicture(backup.pictureStatus)
                    #k6.updateProfile(backup)
                    #k7.updateDisplayPicture(backup.pictureStatus)
                    #k7.updateProfile(backup)
                    #k8.updateDisplayPicture(backup.pictureStatus)
                    #k8.updateProfile(backup)
                    #k9.updateDisplayPicture(backup.pictureStatus)
                    #k9.updateProfile(backup)
                    #w1.updateDisplayPicture(backup.pictureStatus)
                    #w1.updateProfile(backup)
                    #w2.updateDisplayPicture(backup.pictureStatus)
                    #w2.updateProfile(backup)
                    #w3.updateDisplayPicture(backup.pictureStatus)
                    #w3.updateProfile(backup)
                    #w4.updateDisplayPicture(backup.pictureStatus)
                    #w4.updateProfile(backup)
                    #w5.updateDisplayPicture(backup.pictureStatus)
                    #w5.updateProfile(backup)
                    #w6.updateDisplayPicture(backup.pictureStatus)
                    #w6.updateProfile(backup)
                    #w7.updateDisplayPicture(backup.pictureStatus)
                    #w7.updateProfile(backup)
                    #w8.updateDisplayPicture(backup.pictureStatus)
                    #w8.updateProfile(backup)
                    #w9.updateDisplayPicture(backup.pictureStatus)
                    #w9.updateProfile(backup)
                    #l1.updateDisplayPicture(backup.pictureStatus)
                    #wl1.updateProfile(backup)
                    #l2.updateDisplayPicture(backup.pictureStatus)
                    #l2.updateProfile(backup)
                    #l3.updateDisplayPicture(backup.pictureStatus)
                    #l3.updateProfile(backup)
                    #l4.updateDisplayPicture(backup.pictureStatus)
                    #l4.updateProfile(backup)
                    #l5.updateDisplayPicture(backup.pictureStatus)
                    #l5.updateProfile(backup)
                    #cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

            elif "Bc:ct " in msg.text:
                bctxt = msg.text.replace("Bc:ct ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getAllContactIds()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))                
                
            elif "Bc:grup " in msg.text:
                bctxt = msg.text.replace("Bc:grup ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getGroupIdsJoined()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))                

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Speed" in msg.text:
                start = time.time()
                print("Speed")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "WAIT▒▒▒▓▓▓LOAD...99%")
                cl.sendText(msg.to, "%sDetik" % (elapsed_time)) 

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"Mʏ ᴄʀᴇᴀᴛᴏʀ ɪɴ ʙᴏᴛs")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Nɪᴄᴇ ᴄᴏᴏʟʟ ᴀɴᴅ ʜᴀɴᴅsᴏᴍᴇ")
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["Clear grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()               
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)              
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"[Complite Leave All Groups]")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text == "Ginfo":
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "Uni":
	            cl.sendText(msg.to,"Hai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
            
            elif ".music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
            
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
            
            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e

            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"send contact 😉")
                
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Link on"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᴳʳᵒᵘᵖˢ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᴳʳᵒᵘᵖˢ ᴬᶜᵗᶦᵛᵉ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᴳʳᵒᵘᵖˢ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᴳʳᵒᵘᵖˢ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki2.getGroup(i).name + " | [ " + str(len (ki2.getGroup(i).members)) + " ]")
                ki2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki3.getGroup(i).name + " | [ " + str(len (ki3.getGroup(i).members)) + " ]")
                ki3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki4.getGroup(i).name + " | [ " + str(len (ki4.getGroup(i).members)) + " ]")
                ki4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki5.getGroup(i).name + " | [ " + str(len (ki5.getGroup(i).members)) + " ]")
                ki5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S6glist"]:
                gs = ki6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki6.getGroup(i).name + " | [ " + str(len (ki6.getGroup(i).members)) + " ]")
                ki6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S7glist"]:
                gs = ki7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki7.getGroup(i).name + " | [ " + str(len (ki7.getGroup(i).members)) + " ]")
                ki7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S8glist"]:
                gs = ki8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki8.getGroup(i).name + " | [ " + str(len (ki8.getGroup(i).members)) + " ]")
                ki8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S9glist"]:
                gs = ki9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki9.getGroup(i).name + " | [ " + str(len (ki9.getGroup(i).members)) + " ]")
                ki9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S10glist"]:
                gs = k1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k1.getGroup(i).name + " | [ " + str(len (k1.getGroup(i).members)) + " ]")
                k1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S11glist"]:
                gs = k2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k2.getGroup(i).name + " | [ " + str(len (k2.getGroup(i).members)) + " ]")
                k2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S12glist"]:
                gs = k3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k3.getGroup(i).name + " | [ " + str(len (k3.getGroup(i).members)) + " ]")
                k3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S13glist"]:
                gs = k4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k4.getGroup(i).name + " | [ " + str(len (k4.getGroup(i).members)) + " ]")
                k4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S14glist"]:
                gs = k5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k5.getGroup(i).name + " | [ " + str(len (k5.getGroup(i).members)) + " ]")
                k5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S15glist"]:
                gs = k6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k6.getGroup(i).name + " | [ " + str(len (k6.getGroup(i).members)) + " ]")
                k6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S16glist"]:
                gs = k7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k7.getGroup(i).name + " | [ " + str(len (k7.getGroup(i).members)) + " ]")
                k7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S17glist"]:
                gs = k8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k8.getGroup(i).name + " | [ " + str(len (k8.getGroup(i).members)) + " ]")
                k8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S18glist"]:
                gs = k9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k9.getGroup(i).name + " | [ " + str(len (k9.getGroup(i).members)) + " ]")
                k9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S19glist"]:
                gs = w1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w1.getGroup(i).name + " | [ " + str(len (w1.getGroup(i).members)) + " ]")
                w1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S20glist"]:
                gs = w2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w2.getGroup(i).name + " | [ " + str(len (w2.getGroup(i).members)) + " ]")
                w2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                    
            elif msg.text == "Link bokep":
                    cl.sendText(msg.to,"nekopoi.host")
                    cl.sendText(msg.to,"sexvideobokep.com")
                    cl.sendText(msg.to,"memek.com")
                    cl.sendText(msg.to,"pornktube.com")
                    cl.sendText(msg.to,"faketaxi.com")
                    cl.sendText(msg.to,"videojorok.com")
                    cl.sendText(msg.to,"watchmygf.mobi")
                    cl.sendText(msg.to,"xnxx.com")
                    cl.sendText(msg.to,"pornhd.com")
                    cl.sendText(msg.to,"xvideos.com")
                    cl.sendText(msg.to,"vidz7.com")
                    cl.sendText(msg.to,"m.xhamster.com")
                    cl.sendText(msg.to,"xxmovies.pro")
                    cl.sendText(msg.to,"youporn.com")
                    cl.sendText(msg.to,"pornhub.com")
                    cl.sendText(msg.to,"anyporn.com")
                    cl.sendText(msg.to,"hdsexdino.com")
                    cl.sendText(msg.to,"rubyourdick.com")
                    cl.sendText(msg.to,"anybunny.mobi")
                    cl.sendText(msg.to,"cliphunter.com")
                    cl.sendText(msg.to,"sexloving.net")
                    cl.sendText(msg.to,"free.goshow.tv")
                    cl.sendText(msg.to,"eporner.com")
                    cl.sendText(msg.to,"Pornhd.josex.net")
                    cl.sendText(msg.to,"m.hqporner.com")
                    cl.sendText(msg.to,"m.spankbang.com")
                    cl.sendText(msg.to,"m.4tube.com")
                    cl.sendText(msg.to,"brazzers.com")
#----------------------------------------------------------
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Bʟᴀᴄᴋʟɪsᴛ ᴇᴍᴘᴇᴛʏ")
                else:
                    cl.sendText(msg.to,"Lɪsᴛ ᴄᴏɴᴛᴀᴄᴛ ʙʟᴀᴄᴋʟɪsᴛ")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)                    
#----------------------------------------------------------- 
            elif "salam" in msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!Salam","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    cl.sendText(msg.to,"maaf kalo gak sopan")
                    cl.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    cl.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin:
                            try:
                                klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"Nah salamnya jawab sendiri dah") 
#-----------------------------------------------------------
            elif "Detail" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass 
#-----------------------------------------------------------
            elif "Ppgroup" in msg.text:
                group = cl.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                cl.sendImageWithURL(msg.to, path)                                                       
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Bot sp","Bot speed"]:
                start = time.time()
                ki.sendText(msg.to, "Loading speed bot..")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki2.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki3.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki4.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki5.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki6.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki7.sendText(msg.to, "0%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
            
            elif msg.text.lower() == 'responsname':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName
                ki7.sendText(msg.to, text)

#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-------------------------------------------------------------------
            elif "youtube " in msg.text.lower():
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")                
#==============================================================================#
            elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "ˢᵉˡᵃᵐᵃᵗ ᴹᵉⁿᵈᵉⁿᵍᵃʳᵏᵃⁿ ᴸᵃᵍᵘ ᴾᶦˡᶦʰᵃⁿ ᴬⁿᵈᵃ " + song[0]) 
 
            elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						cl.sendText(msg.to, "ˢᵉˡᵃᵐᵃᵗ ᴹᵉⁿᵈᵉⁿᵍᵃʳᵏᵃⁿ ᴸᵃᵍᵘ ᴾᶦˡᶦʰᵃⁿ ᴬⁿᵈᵃ " + song[0])
#==============================================================================#
            elif 'Yvideo: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it") 
#==============================================================================#
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")                          
#==============================================================================#
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.") 
#==============================================================================#
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/0hNPsZGNvyEX9OIz0w4GxuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03")            
#==============================================================================#
            elif "Woy! @" in msg.text:
                _name = msg.text.replace("Woy! @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(g.mid,"TͫͪͤͯE͊ͣ̓̕A͛̍̉̉Mͯ͌̍̽ N̓̔E̐ͮͤ̉҉̢̦Wͨͬͨͦ҉̢̨͔̥ ҉̯̖̬̀Ge̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐N̓̔e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟TͫͪͤͯiO̸ͬ̂̀N̓̔҉̣͉S̷͌̋̅༻=+> ")
                       cl.sendText(msg.to,"Selesai Mengspam Akun Target")
#=============================================================================
            elif "playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("playstore ","")
                    cl.sendText(msg.to,"Sedang Mencari om...")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"Ketemu om ^")
                    
            elif 'wikipedia ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))    
                            
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["Gift 25"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                
 #------------------------------------------------------------------
            elif ("Gn: " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Tidak dapat dilakukan diluar group")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u923fca3dc907e047572ad25c24f1d29b"}
                  cl.sendText(msg.to,"Done")
                  cl.sendMessage(msg)             
 #-------------------------------------------------------------------
            elif msg.text in ["Invite user"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact") 

            elif 'Crash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u923fca3dc907e047572ad25c24f1d29b,'"}
                nadya.sendMessage(msg) 

            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ki.removeAllMessages(op.param2)
                        ki2.removeAllMessages(op.param2)
                        ki3.removeAllMessages(op.param2)
                        ki4.removeAllMessages(op.param2)
                        ki5.removeAllMessages(op.param2)
                        ki6.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")               
 #-------------------------------------------------------------------
            elif "Blacklist @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Blacklist @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"ᵁⁿᵇᵃⁿᵉᵈ ᴴᵃˢ ᴮᵉᵉⁿ ᴰᵉˡᵉᵗᵉᵈ")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")

            elif "Blacklist: " in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("Blacklist: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Whitelist: " in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("Whitelist: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"ᴮˡᵃᶜᵏˡᶦˢᵗ ᴴᵃˢ ᴮᵉᵉⁿ ᴰᵉˡᵉᵗᵉᵈ")
            elif msg.text in ["Unban:on"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"ˢᵉⁿᵈ ᶜᵒⁿᵗᵃᶜᵗ ᵀᵒ ᵁⁿᵇᵃⁿ")
            
            elif msg.text in ["Blacklist"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"ˢᵉⁿᵈ ᶜᵒⁿᵗᵃᶜᵗ ᵀᵒ ᵇᵃⁿ")
            
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nᴏᴛʜɪɴɢ Bʟᴀᴄᴋʟɪsᴛ")
                else:
                    cl.sendText(msg.to,"Bʟᴀᴄᴋʟɪsᴛ Dᴇᴛᴇᴄᴛᴇᴅ")
                    mc = "ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ ʙᴀɴᴇᴅ\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "ʙʟᴀᴄᴋʟɪsᴛ ᴍɪᴅ ᴜsᴇʀ ʙᴀɴᴇᴅ"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            #ki8.kickoutFromGroup(msg.to,[jj])
                            #ki9.kickoutFromGroup(msg.to,[jj])
                            #k1.kickoutFromGroup(msg.to,[jj])
                            #k2.kickoutFromGroup(msg.to,[jj])
                            #k3.kickoutFromGroup(msg.to,[jj])
                            #k4.kickoutFromGroup(msg.to,[jj])
                            #k5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    #gs = ki8.getGroup(msg.to)
                    #gs = ki9.getGroup(msg.to)
                    #gs = w1.getGroup(msg.to)
                    #gs = w2etGroup(msg.to)
                    #gs = w3.getGroup(msg.to)
                    #gs = w4.getGroup(msg.to)
                    #gs = w5.getGroup(msg.to)
                    cl.sendText(msg.to,"Fᴜᴄᴋ Yᴏᴜʀ Gʀᴏᴜᴘs Iᴅɪᴏᴛs")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ada Member")
                        ki2.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ki2,ki3,ki4,ki5,ki6ki7]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Hahaha")
                                ki2.sendText(msg,to,"Fakyu Sundala")
                                
#-----------------------------------------------  
            elif "Ghost out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass                                          
#----------------------------------------------- 
            elif "Ghost in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)                                               
#-----------------------------------------------
            elif msg.text.lower() == 'reboot':
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"ᴿᵉˢᵗᵃʳᵗᶦⁿᵍ...")
                        cl.sendText(msg.to,"ᴿᵉˢᵗᵃʳᵗ ˢᵉˡᶠᴮᵒᵗ ˢᵘᶜᶜᵉˢ")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"ᴾˡᵉᵃˢᵉ ʷᵃᵗ...")
                        restart_program()
                        pass
#----------------------------------------------- 
            
#-----------------------------------------------                                          
#-----------------------------------------------
            elif msg.text.lower() == ["join all"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        #k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        #k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        #w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        #w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["-","Teko","Aim"]:
              if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        #ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "Asist joined"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)

            elif msg.text.lower() == 'Sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Pro1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Pro2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Pro3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Pro4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Pro5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Pro6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"  
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
 #-----------------------------------------------       
            elif "Pro7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            #elif msg.text in ["Jinlip"]:
            #    if msg.toType == 2:
             #       ginfo = cl.getGroup(msg.to)
              #      try:
               #         cl.sendText(msg.to,"Pamit Dulu Ya😘 "  +  str(ginfo.name)  + "")
                #        cl.leaveGroup(msg.to)
#-----------------------------------------------
            elif msg.text in ["V","Off","Mole","O"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye All "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to) 
                        ki9.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        k6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------                        
#-----------------------------------------------
            elif "Pro1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pro7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")            
#-----------------------------------------------
            elif msg.text in ["Sticker on"]:
                if wait["sticker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Sticker off"]:
                if wait["sticker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Uɴᴀᴄᴛɪᴠᴇ") 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)                                                  
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["linkprotect"] == True:
		if op.param2 in Bots:
		    pass
		else:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti) #kicker join
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    ki8.kickoutFromGroup(op.param1,[op.param2])
                    ki8.leaveGroup(op.param1)
            else:
                pass

#------------------------[Welcome]---------------------------- 
        if op.type == 19:
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            try:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki8.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ki8.sendMessage(c)
              ki8.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki8.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ki8.sendMessage(c)
              ki8.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
#-------------------------------------------------------
        if op.type == 19:
            if op.param2 in Bots:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nWᴀʜ ʙᴀʜᴀʏᴀ ɴɪʜ ᴏʀᴀɴɢ ᴋɪᴄᴋᴇʀ")
            print "Kicker Tuh Asal Kick"                   
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
             # if wait["protect"] == False	
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.sendText(op.param1,"please do not open link group-_-")
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki8.updateGroup(G)
                    ki8.kickoutFromGroup(op.param1,[op.param3])
                   # ki8.updateGroup(G)
                    ki8.leaveGroup(op.param1)
                    wait["blacklist"][op.param2] = True
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\n╔═════════════\n║Hᴀɪ Sᴀʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ   " + str(ginfo.name) + "\n╠═════════════\n" + "║Fᴏᴜɴᴅᴇʀ ɢʀᴏᴜᴘ =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Sᴇᴍᴏɢᴀ Bᴇᴛᴀʜ ʏᴀ 😘 \n╚═════════════")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            #cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " \n + cl.getContact(op.param2).displayName +  "\n╔═════════════\n║Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " + cl.getContact(op.param2).displayName +  "\n╔═════════════\n Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ :v \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            print "MEMBER HAS LEFT THE GROUP"
#--------------------------------------------------------------
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Wᴏɪɪɪ!!!!! " + "☞ " + nick[0] + " ☜" + "\nBᴇᴛᴀʜ ᴀᴍᴀᴛ ʟᴏ ᴊᴀᴅɪ sɪᴅᴇʀ \nᴀᴅᴀ ʏᴀɴɢ ɢᴀᴊɪ ʏ ᴊᴀᴅɪ sɪᴅᴇʀ   ")
                                    else:
                                        cl.sendText(op.param1, "Assᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ " + "☞ " + nick[1] + " ☜" + "\nNɢɪɴᴛɪᴘ ᴍᴇʟᴜʟᴜ \nᴍᴇɴᴅɪɴɢ sɪɴɪ \nᴋɪᴛᴀ ɴɢᴇʀᴜᴍᴘɪ   ")
                                else:
                                    cl.sendText(op.param1, "Nᴀʜʜʜ " + "☞ " + Name + " ☜" + "\nKᴇᴛᴀᴜᴡᴀɴ ɴɢɪɴᴛɪᴘ \nHᴀʜᴀʜᴀ   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
#-------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
                

    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

#def autolike():
     #for zx in range(0,100):
        #hasil = cl.activity(limit=100)
        #if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          #try:    
            #cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
	    #cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"ᴸᶦᵏᵉ ᴮʸ ᴸᶦᵏᵉ ᴬˡᵛᶦᵃⁿ ᴾᵘᵗʳᵃ\n\nˢᵏᶦˡᵉʳˢ ᴴᵒˡˡᵒʷ ˢᵉˡᶠᵇᵒᵗ")
            #print "Like"
          #except:
            #pass
        #else:
            #print "Already Liked"
     #time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def autolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
