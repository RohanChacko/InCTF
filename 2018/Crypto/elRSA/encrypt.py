from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from gmpy2 import *
from secret import x,flag

g=5
y=31536853689832602395346579481926020012099896103001065768198918987056883292115821849640385197184490918876558294967985139470377216296955453855847741523875341630579966560813213505047967120467121002495669790292071191983014475638554310886314249079793026730637077563037932539727644309820312370667781912363866238797915795156660290659925541622744317391134708493098920208281688510485081481768037269334124243047896595749465671244892934808237828477292755833581906024085174509689361590250564083802312272236472204812084775503365848798329178668302602139125616310133805774443397117570174150233351415298111908450871658343205070925327L
s=pow(g,x,y)

n=16670686215281612814941562764308755263128627044120988885563299110635782433792170614444096250879445982518715915537321626243364100768142433140123649413904542724970304551227196423027709927910284420430624912791302518248784566619550335156818429186950550449453175412859301366956616970170266030597129915738075183577714222233140408160845119084697898788709191092889695866444291208140742604271244707732106282812749310339799673462058634497854537019414317493456986092169462233617020984976470290094223570034317770843812556339854406641917684992052392093487947262411609752038982497035914462429306915274989496178658928703952692715583L
e=x
m=bytes_to_long(flag)
c=pow(m,e,n)
f=open('parameters.txt','wb')
f.write("c: "+str(c)+"\n"+"n: "+str(n)+ "\n" + "s: "+str(s))