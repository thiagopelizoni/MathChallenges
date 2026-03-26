# Problem 54: https://projecteuler.net/problem=54
from collections import Counter
from base64 import b85decode
from zlib import decompress

DATA = (
    "c-mc^NwTEM5<};)id+LdLktEOj4;^$T0Ws8aqGWf)y<@d@bE^Gdrs@`xqs*SoA+OL|Hkdt+`oSNwfApXOTYe>t^RX)Kd}DB_1Eve"
    "Y5P6f@4QR9|Hl0{=<CP*yY~A3$NFow-*lJf{p9|8uW;SJhwJOF=ly=TaH;o;@3)Tk`tL>F59oH?UFx51-Epg5ob){JW7Ox_%kX|u"
    "SAHL$+3TO)i}ZJWlI6Ycd-t_|;Jw9r-}e@sJ~`g?nMb|I@IL=m|FhHMU2A>8b1(1Xy%*_q*+!q4w|bpL&-^}HeaF52=lg2!x(zIp"
    ")~eA0zE9QPzVG{9gO;~l%cXaGpZr~@=6xQ$*Qw`x*Xpb*_M7i|uXp`hUHN^Iu70MpYki~ldEV7{*YN#Vr&sRk(v?Z~8g<k6Gw<!*"
    "XS=jz{rlamF6^Zzsq3T1nDm0zUEcqB*Y;h6_wIxC;?d&NW#3ApzfM}fN00Zu_^h>RxB67?(lvU>W3O-2$S~@Q>~#m<zfLTXo}XQQ"
    "4QAZx4nA7jy0E)$z1HiW)k4Zr*Q9>^ec5-l7q4Nx#rsCR{{LOZR=eO8)~iix8MI&3RAd<Mc2t9udA!g3{^xt^rdooow$-N^wJFnH"
    "PA#eS+E(G!SY_>-EcvciJM;{T)})&BR`<7;h4)(UQ44bDjk>)wvj0IwJ8LgECe@Z+o80PM-mASAId;F@sO7CYxO)fng7uZ(_reJK"
    "yROx&hncnVot~}LlTTZ{?<sq}WT<r$-xu6<sk@%;_c?p)T=!)Y&$^i9#4TtC8`;LJk3H4WN<BpS?xim-dWB1V;5|q0w_1Jv(3$P@"
    "#YHB1X*CA9g7+e=j{L0SU(ecm-?*A%^#Zo~Zd<)UUFTD#RS%I2>|K!e;&c6cx$qS^_3vs7dbaw3*J8ErmyEFPk+uvQc;B}kdA-!5"
    "Q}F(^9*w=O`Ri3W?fW7_<#;}N@lJlD8mg9h(Z;oU!AAET)_Ou883vC%%I(Z@N}QBKt6GonRv)1H8QFH-BN_Ir6ExO6t<TI}H}6yF"
    "MNZjaqy6IZ^5o@`3%xeG9o+aN5C6W=sn<F5I<vN*)l>EHb)2~K_BrAip6Yzcp>^(c<x}r<$#{mk^5uOtTwmQFnc}52sjmL6`+LZY"
    "n>!n)^FCE$tKY4zNo#xQu$*$g?`pTYG8;7NP!G5Tna6k+qQIe3(C_wyi(j+gv>Q3khZomgw7dPJU-?#0&`o>oa`h@&qR!@BuleX5"
    ">-D$N$+cGNt%1PjsO2tOUCB{rA3u4@7#@Y%;eB6rpS9XpglZ%@HS!yqqvRvA=hSrd0qXv?t4#&pHN^wJ@d!J7v?i0xc$O1>@K-C3"
    "r&ZD#vXwPxZgqdJ+aZ`pv}m)=`Y}bitu8_%e}yyeH^-whZ*j=&5bxy5-isF&f81?{gW@vh{nSb6wOpOf!ll5(hMuy?iFiQ<qNg1k"
    "85O%_5`6yJ?dxjvUu(qacOTDD&i~Y2D5<F5ZFS8>zLZxcGkNbj=_`}|r@8IZMqT{cs!g`sdaZBD7L2l%cL(v1=kCZ(tie@YvJK+$"
    "C`%g@m$REinNoet9=9x)#W8$i8C!GV?sQ12`RSRPt;U6mShm_pcJhkP?zQT*YsAWPbLutagyQQK-SN=#^fK>ZtG>O*Fm!Am`A<1I"
    "S>5KK|LDm_U8ldfk)BFNuOmX~Mh{+5mUC(~+RcgRq&U(m4o*6cyvU%vYqhF<y^%bUHnCmtLV7!Wpws@I_;&e!rLQ>@Zx*!rjV`_K"
    "B9D6dBv#+v>BEl}zrD$ha7u-}YZDF6&4*W+QavfBo@!APyW}b-#lB8<)$TTa((FTDJmjByttyr_+|H2>o%i>d51pxln8m~EMmk?L"
    "F7&!ltBjG*&^Y<588RuvslSeLL5I$J-N8FvNLx9Qb^Dcd7IX>**%B#qi>F=d4%Toc_bxk>r;-WT$LbKB90Xmzm$mfD83r;08Er4i"
    "oL75b(z!#2y1D(<qx=#l^wR24Yh3b>O6hC-ePr!ea>o%%B~nkQR`1-M1@+{USfDaS@|I3+tsxWEZcfT$rv!RJUZ-?RFI5QKhjNKw"
    "cPe$rk-i>j+3fi*MVx+f{y(e6IX8QQhh$h5J3Ei6`#bGU1_qteo-#yv-KCR4#)7H$T8(yB9Mtn%veji}@$05k1J>Ecbu?PBO9$}O"
    "Qop`^SbZc1UG~~sl-1MmUYU&Ob~HS9Z^WQD_-LUn`SyWOxFvomE(|)YR}R;*yI^_Os)_Gn!53}Qfc@yo&+S9x1F|~_9QS&TYFdsD"
    ")JwHEcJ1%6JL$TV7@WM0%>Jzi77j0I%;vnY-~2|i7GcB>?~bP@#q3(hYI-f*sQ+v>yMjhBwBMZ8UYotsyxZr@n{$s&*-=YmU&(a~"
    "k-E_%HCo<TYg?-roxzc8dG&F7TpZPm@w#0!9kRNa;&&q_sZTYoWcYHYDqEV3biJM<pB<URpp|^ck@ot`k5>L#y+k<Jx^cQP{(0G5"
    ");Y&kh5INyX!MXnQY?zKQx#vYFFpz!hcfd)7kp3mxjOlrNJxMhltni}18~u)#ay&1HLaQ3ob<aTZ6Frh^4_a`!lD1s@u{CwB3%}p"
    "uU;F9(<6b`!j>jc!=6NoeB#jFif?zV*X!b#8QcA?<dEd#itim)`_e^TbjBET02|^dD9T<>=(8Dum~@Dm)t2^t_t~BNEOOx8N<FSC"
    "@3kIm*jasyESiw|o}*UQvgkGO53Sa=tt(UCmpt4xlnji(G^j2+<#Psnj?NLj^xcJtQz^&T1Iye71bSV0P72-Xr6{ypRU&8bkcS6L"
    "Rah-~uNK>G$!{qc2=3J<6hgCi_V#`?nC@Nh2?O<u%wXJ%fOYaYGj^EI^zuR=3Bqlh7d@+^RWGOgdhbKa(x+-Td<vA<Y&GAQHUl!F"
    ")@lrrcCLP-W3>mK|4E@=zd_AK6sE+$rD(y0U~EpG9;}XYS9hnL1)vYY(4!bV?*z(1A$)AE6qYP|ulU=oq;NK^S-I||tYaW^10d2("
    "=a^0P1FGmTOTz9#!lU)P^u9nJbBc%w>`rlknr<QcrC5+Bte?^820pq#cytm+hx@|z;b0pcSXZtUt}6N=iTAPFs9Npj``v}KN{=+j"
    "OB_CcLa3C2f+CV~5GLy0=^RmD_WBkT`e_eeNC*!t{*{7d#!<+t^m@+jc7VhDdS$slPsRZCnoD-GQ$4t76Q_-wxn4gxWX+&vYPz5t"
    "M9fit#s2%iV)JT`_oz;xglTtUZXB_Rt-K5CKkC+<P2ww%>n;G4u~R+4?)G0<8B$Y1716&{twHj0>Za72jVxU8x;|B>?H+*zIBqV("
    "3n>#>*^+#?0a}seOdR>u@v*~f>ax^l9*AOV?B~PG73ny+=Wg$P>EcRvi@cUAwI#@Tqi1-liGxI)^kX&Z^4wrPH8Y=mYLc<<t~=g6"
    "I<$;z3Yms7D^|6B_tYypwb-17wKcNT?CV2^y3MH+IoK@p<B`WWspVHce5)$Pkv&QKC}-R1^$*>bxXEgFdb@6OZpOVj?ZR|B-+NX7"
    "(gM&2kkXM(;I$M(uPkgEXGQJykgLeAUaJ9f+{+>lun1uWWB}b|-%nO=^GP{2<A)#WtIDo`?NcIw2(_!N>y4p{_KsQ%t2>C-)shQO"
    "3+}PR;CtYOy<#$rcH!Ebq8z&W06MLOYEvN&aY|VGs0cFZts5;kXjm(pf7Y^4rU6pnqv|@mXMZzPa_Bj)JK<PykaD0Uxn1q^`*1*W"
    "IG|&90^?#<b~Va3l8wxXmA&5X(HqUFV#eLsS8KvW+yo%}W?}^dOpD`~^5`pbNGJzrRwJn<$FNiSEhMd8ndJFc1Nf}wjCxhpWb!ad"
    "6A_IP{;s(hCytjQySwy(OXtWX5@%dS1#vTyscLK3;$8vh3MX>txP7tmNg`Cw!d|a@rH+{65(gcYp16>_tCM4gU{V$#PDFnK3<STL"
    "R}!HDV0CE?zvn+?A&+uzK;UIHKS&Buoy=W;SgG7e3tNn8j~88?6kS;>aHRK*CVgez%)U`ZHO5Gbk^j|C#gV*BXH;Yic8mi;Wkd}H"
    "vQ4xdZtrrx+BvjhEujWjkU{G|kYMZuQlL{<hvjKELw~2DGd^mBcGOzo&ky<bL-t0YdO7<gDiw2fn|V)2pJ`)Ls=rz`Kg_9%5O9T-"
    "*ZYD<KX89r=+WEN)1Zd|li{rOM)vATQrdv>k%Yrr%|b5$BtfT#U`?lZoMrWvJ*zpI;WnZ0uJe+mgLZjf)^yz7J;D{Vn|ZWOe}cz6"
    "lwD&9y%HX(uu1-Wlour|IyKUc5T2&&APDfZdVen+w2Cv_erE94ORgKUJjLUHu>c2=J59UKZzF>d&Z(y&iIoEcB_4tk!hnpoqwrhN"
    "<HsH{c`~%yVCL(A^=y7@Or50n5ZZIegg937=1|o+*>-J(ZzsWSg7{6!%%M@5m6K%<L+ng}d7pOk9kU$TiEE<n&LO&X=U1eWi;$Bg"
    "ak<L@bh^H47j{?-Wk<W2<yt{(H5&mgo3{{c|FESL!dS9mPyj~7Uye2z7f*{xABt8)RSxN;7}_L>nuP=c*-<rc@DoQ0$n&KCC%fo^"
    "vo)%YzcA5;Lmw%2wqg<%C|J9U0bKHRhfW`9+qpaIgQ9A5Uovxmh>Pc^Fqg%)q3uA)@Jl)r1q24_unTjsxRNRyNe;+q;$A4XswWTz"
    "0BzvGBf0&l{lyDW5fgbk%uIPZMH45K?d~?<`r<lzw?LvHR&v&ai}Ll6{7q#VS9tVBfV4yz00#iusv7~H)Ej}f3>)M^eda4=_>p7)"
    "6uRHc(Sv(~Zb5&KJCs?i7of<W&Ghj_swUrlg>IfnU~Zf4D6S1ZLu46ms}33;hr)-+?raiN!FBzO<Rd)5U9@2^Yre5LooM7IS;=7q"
    ">nPpl0C!XK;wvFfYs5ixF%s){Cuur3Wr(8SD<P*?@3YzGz*Rjym?p0qX-<wP3K|l&uw&%UXAq<=)e7&ph_i0PV_pVZ?7;i2G&UhG"
    "#ihLy$zFE>x}QKshCq!Y=&68p47%(B5r7s*3<5PNm>4|WLRb_V4ob7=d2skmqQI;wrb|i;tJQ{ReuOf03ciSBrY%Ys)GV^MeziHx"
    "tKSG*rA@pbzAv~AtXi1N2oR^dnvl`kUCY`jia#=4hAk^Ch&qU&zy${)fz|gVk!WrUcor>1BObP)a9#}ub#c+vdN<c)0F3Y*98#rZ"
    "#mbz-EL`QJq~cLb!7ani&%{>Zh%9ytJ#pMd+ekhi<qV$!r<X^1ZYz!^RRoY_z*bk}Oe$k5e>8>AA8w=H@G@XuXu!z!M_seoA(+gU"
    "wP=lq!mFXPX>)x9>IjN>X)9Io*Jtim$Ivcj1L!fyt8g5MBOR<0Y?033vYTO<;~#L^<_K=b0%F9eO9?a<E_z#Nbgrhwi7)Tzw)a-i"
    "I_a;U;%J0hj0~(*cDL;I0JAU|*t7<sXSe!GB7_3R-BCyEe&2_JLa2BfuoRsCgi8`i+*yX_H+>Q^WIv_<h@sn34N3!{g@s~`z&Zu_"
    ">8N*<xnV62Y9dl%1BL}b4yZC~b>-RK_-mcO<_Ck|;3$!~nd@AwtV0H%?QkAD=ZJy-!(km_4`K7CI~d^RKz~Zzfy@c=Zb+`u2X(nP"
    "Q@3-KJ{8s}p4~7D9D&RRkQ`>JU#&2lw4Pm3$|iLRXSTV`q2qQQRk-tQ0v$B(ijHg28_gm2VPVi|bgMlfh5?p1>%GhhZALFSbhvcB"
    "JA!=PW*>+SbF?3*!i;t%u}6Eb;IE`dns1X+ooO;4HRTMeb7s7>{n$U)CdP)!bl6OqP+5bjJ)aZ-+ylTzNCM?2e_CQTqErgvifMNy"
    "K#c<m*TBQt@41$wvR=e3HnFRbbo6$CBcW_T#RNs$ujb$`O99IevELBz8JxUVE;{daL3mNJ{U~P&YAZCKBs>?u3+xgp9||R8OL~h#"
    "T9+f_FFDv4e_J!Ly}%}LJKXpa)`n_vqEt*Z0aYp`r1<?jEo2R0v{S8NE!G{Nb$7BY^-%!^>^EoBtsWlKqVkfrr7ye%EF|S{E5sH3"
    "l68Q(CL)kW?@Ks_x*fxCwQH(l!t3n>uV0<~!&?mj=UWsq+ozZ+h7|DLw>43%JkKKTX^4!0^o#;Z+_bBSes^|Cnnb<xi1R|p(1!$U"
    "qQo1Oeer}(D&ONH5T&04yBOqKP+u=*RlHV|pHr0NvlCrcF>LX_I%Hw^1!dF_?J<uxZ_a{Tu<yn;PnkDGRwvaTfu72RS_YqKyV{*u"
    "0YKq_K~9d_96gd1;=V<^x^Eu|WfK+&0er=Bw?85Avi)hWTV=Tb-9)PaBq4{imp!{ej5voU2lobqKf*6xn<WGn{`ofgG|4vRe*)rs"
    "TVK~C9qo7kSCqv{&doZC&c4^GKPxW6nBXLlj&yn|2xT<1FxmqyNEP24Cwzr|vTjW_Ng{OY=HR4!mX{V<+Xlil?-p?2xxLOPLs}W+"
    "EVCE0Q&@isK3VhINBE5z({2YvKF>C>%crmrio{RZ4jFnV%Wb1PhvFyLVZD<q_6bB!@pVzrD`NyKrHDIsSJvpM8f8JCtWZu}KvX5D"
    "1*ZX?(?^C%4Rz@pb+EU$CCbj_bjq&Psve0<tdF8dq{g|d)v<ICrH~4N@&pLNbo+mB&P9p^B=<w~&v1*2awJ%)C30U%QS;+c&>frU"
    "voXvy2E5$HR3DU+q*bdOBYHDLMBQyp96m_wiRzT(KTYyv3tAM}KZN$#Ek1c}IN5@$CziD#R><zGLMO?LoCd+ank)*GC93-~>dnj7"
    "Dbttdpc9K0U2@!F+Ejtk8oAAsXt&yXN9<wcKx1sSSlqjPD?s%M{9e#Kl7LNNY|SG}QN{`%MreH^=xu2n@=S$5URd0vGuVeZN8x71"
    "M1Q6C2fDeBeh=Vx6f!oO4K#h+L}Ir{AA9U3q{wxx@R90(Y@`Vu-spUR$q!=F5Ft;w;{?~NdVyTM+s*QzlW*P8P$*}{;E(`)Cslwv"
    "A=%@H1D^=qWH|ufvkL^Pg=hFaG0T8vSC}}`EhT;h=muadQeG3m?;ai7KQ0svC#;P;@D;s5llF&sbwzm!CGO**5p)@2k-vJhbkrkP"
    "uo@`N*E6)Mg$gc(z*S(|rQe|00kjamL9iRe($efeJ$QU=EcH5N4k!&C&hf-cbVBoHf?cRyYN7#FTDDE;0gOrM(deX{w}o3onPs<X"
    "Vvz?no3@&R>r)G>lq;WbYgrw^-Op7Qr;z@EJn%-x?$g={Q>FKcHWr0@_mQ2ed((#G_Gp;Nq9?@^+K$fPkZ2DCr<6V-76fCcE;(q2"
    "YId64#?`^S|LjxBfd=&Qwger(N4kz;YyAEviWJF63V3oG(30+_6pV$^$#v^yMNp@ex%5<H*fc6-lvJu&tP67gAT3cz)ae77B0{)!"
    "vzd-xie*CzpO5|No#?6y%$TrIKEkDrRhb;bt*e3V#J5)+MKtFqQl9i8Ne5eae(dl;UVHy3U_Ue!Mis7>vXp)ejK6VzR@w@LP9HF{"
    ">1%^Jq0gdIHgcwPnk-+$)T>t^ccM?E3FB-eP*^>vGE_CeD@}jm=;?P`T}}eXcjSbt1!hk&#_@Lh1KjcQ@rHC~B<ek?yUCY6iN%@D"
    "plLTkMUpwkC0YTfdSQrO_t;%1U9M`~GetGgq>Z#Or(i`llqD!AngpG-0x>bh_Bgz=o6brfsRO2dMi$u7Pj|a(=34FKr%(MW2A?e^"
    "qIJm))L2)b<j4&93Tc0<Q%1HxeY(UsU=qh|g_ZM-&3$=;JD8lu;+E;Gydu$DR`&r}9Yn&Gs(+Nu9C(MGR`O)@W0MeO=wm7loT^#B"
    "%_o%O|0&^t!B4Hm^Pz}twJ>7&h~rz*3kl@g8-l1O6aitY1tiC#$~)n4(hxdPj;&_&MCrP#0<qutk7tmwNa$tMhMbo(Kr~M^+|I1V"
    "Pq7A|#A>W&JmK*n7am>Nk^rcj)$q$=`Ejw_Q7_oXy;HDs>Z<6Y<UAt}pao;3%ODL+07Ora1o{UZiTJ?kRaH1BHUpj94+Cj2p}S1!"
    "Oe8dLoDVNo;dzGDxe7`9<Mg|Jci1fH8PZL5Iv^HmYGZVJx(@(&<0sMW_xUTS6y1eia(ivoj6Ig-7BsQ+ICQ*h&eSQKknDQAU4EXo"
    "+W{6~$OJg+YHlm!$IYA<YrCYe4)j||ctK7N&kh#n_E_~>!E{VfPWHF+DEXo?hZ#qC3;OC#3Y~q}kR|Fz>_@;|S;841S97ts`F&|i"
    "G(DOXo*lN#{sT<_?>`Bnr!opqCgd55Q4weL2N2B%+1*a^M@7j#t>0*$(xoMIMLFRWAzvRx;B;d}p%7SHOeq@P?#6mlJ5Q0ykl|pK"
    "D1J#zjc@Fc{qN>As2%89YW|_yMAa3V4z5p(ok~Z;4GNzhLoiLra@9Cl(5o-&r!E$=X|BJ}#Ai<7b~R_;E^Kp&zNOpUMT<QCAqQUF"
    "$Oe?uCi#3VhYl11{X@IW?zC`JJnGhPPi~NRyIHM6VgJMIbhk}TEeT~@1HtXyreQPBb%^18(oA|qQ#!b8tlu4ixDHtgGrZD2b5aP1"
    "AO>cmH2I;67j2`0gQ0kLu#cjzi{#1rqBV%kZN3;js9)W?)C#-i5Fv*%{AF&=8jL>T_Bn;5u%qHu@zq85wYur46|X_BB|eaTC|aL{"
    "R}>I_7U5c*hfnEtUv?L3ZYK%VD5YO%S8r~AdnK;`M@%GWQqH63gD9Nf7gi@2c>XD(i<&>EN`(eO89PD}L2V12URDET43}URv|=@C"
    "7+bzwd>uT4YMdpQuzQNrnXZ=DLQUQ7E`CQVMFD&Yjiue~+z-Jy5TB!DK=>wk3!lHF7k$#MMSnVIq^SAoHz;{%tiS-`NR7xDioad>"
    "qp^AIxk(RTmw_RS7Z{YOcHjm%(bWDd&U0I@(xg&A9NQYsEn@~~^mMZCHhYPP3JZ0TT}K(%M3sF7CTjGi2tOJ_yTzP>W%h2gUu+Vk"
    "OJ+-L`zhqX>oD>mb^81@%*sDEX-T$FEoJ+dz6mgsS#I#S-OP1S4}t_n{?UGZLv^Te{xul#?JQc!SfQBxI^sVqlN@+CZ!5{6+c1Nf"
    "8-aY@9{gg@vw8Inp?ODiVvzMnM-FO@sNg(;CRD;hEK73`qKF}i1vwULAmNv<Z@!I;@DP%~|A<V)nJ7ex0YrE?1bL%fu7x(0=V$x^"
    "Y5^Se<YKmfT2uT^>8YWav5}sE3&N65?v-=5jt84;?&E`iXt&@wyLomBx+yxJWpnSLH9y&l<zHSSNe(Q)kgCLJUiz$?$R4`1$Ii0J"
    "E}7mHf$OqoUcu&6q)Dqa8K4m9@^x5u8D(%Ld%VPJ%sZLM*9iHGjL;k(84ImvJi~+@DJeJ7lrasJXc9PC%W4pk+J~}nRMtoG36Z_*"
    "4nXA3eKee16e;w5DB6}Lr+Y|Mwd__zx5755m*;>Fql=XKU0OUCk<mx?zeMNO0R`-ToCT|m%CSjB|D<;e_oBXdtA;4(uG{k>E)&^>"
    "7KzJ)Ypekv{g|~!v``HcBb%W}bgD%5nWL08!!DB_xL_ZZI08cG<3=4-U`Ln}J<GGJ1M85Vh;uln=Z!e6kT0Pyhs}p=(MwgE98yrg"
    "U!YdiL?c&Ec%kX*WHGVgOoj(0P>vY^bljf4aw6%x9UvNy7;-1(fBKPovw`Kv5DY3H+C3;bm?i`c?Ea3`{rHl+mMLpR+6+b8W5b|`"
    "tBVCRx9w&X-w_Qnb6r?`U<7s36p*etEZZ1TTWDJu)A%q%RQ$x%k2-_1>u47;Jg}0bg0{TLPPLnxe+4C(<7+a9gluy(VqcczW7dK1"
    "HWF=9!F?T0s5}h=v1KoQpWZa4D@-BNRT&x0Lu7cYe}pEUe@uTCfbC$mi%zs+dh|BJaHiSe1P#cvkUo-c#3%A01=;@)fD!oJx&nO8"
    "W_SIh4Rdr`O1&~A4-8!w5n#szq)@{{6l;ygF4bLFqCSPnr~4S6xsccGE}+0w%;ixX?`C}FAnojk++%_5YNFd|BN9{MQM%wf&1UJ&"
    "7zI(yzK{cbe8lZOQ`IsBX*%77t=lBc6wK%fR`<M+S}+iU**k6cGEmJn)4=4h%bZ5?E=<t%O=%OCx`bO?qID-BM+50nCGzz)!@Ca6"
    "-kCOA`xtve!#}KM;jIJQ{=jWDXO;OwM73N@BcXhNE1!~3A=h6LU+9{lguyw_=#9z5q~|}KhZ{hf_8_0PXF6FZ7%>u@S|__gTaJL_"
    "+)cU8D6BkG>aPYFbFvOGt$k`D+TYMiEAkeyM?6WB0`{<m)78YYrL5i!S8|R>1&`$3?fRzy8+Z3ggA?-B6w!23HabuP54ollmpoib"
    "<KcE21+jZfS=#M?hz(vEw7hZ1F48O+^suxwYP3@|?2@5&$7W!J;fI(0N~1Bk%Jj8XDbG1JbA>n`=&;#XS;4~`nXH9ZY@D!_lqBxg"
    "`vw$<U@b>v&y#J5NsOMrK>09*_-iwGtzX?S*QI}?kIvThtn#ZR0P^7>Z)W^YDcBMGKwLJPCjg*QZqSFPBlQUz+pSiU&ikLve~j2^"
    "T<r<z{lT1$%uo_=q`t+#Vz4mJ`eE<sd%Dw^n?gwkvvipsNb(N|v$)y6pvC1<=mUWoL=l!Y%5z{|!trEe$<y9YowWh7Xj||kz|9k="
    "oF?rag)}JsQrEQc0JIed>?%HDtF?1o$XrQ4jWEv%C~kO!a8!+hVNkvig%SPsLR|!b8Y;wGXHS7Ba4Vz!pG*wti;hycd>EDA!bEI#"
    "jGeSw$mRk1K*h<KJMk$X52OuG+KZG#6?&Zzw6wI(N2WW1o2^lWCB=e%Wf}=39#k*h64fY*!827nsm^6#t#c%7sZT9`q;c<DJ+09i"
    "^4m&}&UmjGB7<GoL4xd}x@?Kfa0Kwr4QkR1azSm5=NU~6cn;O+=2`nggZ8_1L0v?%lEu1cJ$Lt(Qn_4)B|Q^t5kJ_c`4lZHzyke8"
    "O$d7TOJ)$IU=Sg$tK|W00wT2gEVgva)H^Vl+0D*EO}D@PKAg62T5G6|P>M^&YIU1uW**9dzA+a@LPE*Ss;!>&k3J>}gab84aAkVQ"
    "ygNZ68vzn0Rq#MR40}uWcg9elLTsZ&zch2e>WJH-@h8tbYo-KDTpvjroy(%;3q4Rxfb?d~&{|!23Xnp7S(kZqs))<;!RZWZLJ8wp"
    "mxVEa>>7n|mo$64-Ld{n0CpB_jJjCmySu#w2I?|~=H5etDj74FXDf43rsWGgX``6rkr-j|1Y}0~#bnwswe9Q)GoGb@qKxsOSjZCH"
    "DWaoEo`Df$fB+!gg!oQ;_mYt;T|Cw7d7kcF!okua{d~;q>N$`@riaZLE+IoI7KD6)Od^`+(7NMhh=kScLiDg`3fY<YpY7K<czd1<"
    "=m&oL`qb};1engTyV^pTd1koBs9Y3|_4p>E21xNPq}i&=us*~yPuTy_@STA~K*ev`YO@Ae-92)Fsfle!Tg%BpBB<N6d?TvB84#uP"
    "mb8^QOF@s`^D&9~>yQ#=3{3{oC<o{~c8*ARNGFRxjDpm;%d~2k3;JQl+xg@H)*T$uNZMMK40olOagOjqg4hD^JAZ>KZ}V~8r=iL`"
    "Rmjk9sBfn(gRg-7Mip_&da=?=dgqbieB!-9x<01gppzK@w>PW7;a-{l%)2kST92aa_JoZdlrl1mW_6$D5RQPMh?mpL`pg{I*}W3t"
    "*<rrKS<}bIZ~zDh=4H_l$uxi=M;k~7^y5n79&uA5Lp`uE^CR;!2ZlR+EnvGRT#=u25n*;wqSkoy`JCO2DrR1!%f-JPpGt6b(u-~+"
    "fyo08%~RZdU&{ZlWAtlCQQ=VL@W`i83*$myxot!ReQt3vUqu=lyzA)^nx08=xr4QQ)Elh?^J;8FaF*39OSH{LfLX~AJ?8{nD93+s"
    "BYe$ryEOiPJ!?az*)S>H61e^Mbx1+|pwO7&9^HMg+IY~nyO(@7>HPI*G@CsVV@8_HlYxGEr0aV!CZ$7Cet$!oJz?@2kltk+x~^tr"
    "2)g<sQuD$6O@+hNX7$FXb0vu^L)yA$bL$DO>mLt${WDH{h~9Eq&EUgFPl2gjm`Ld~eK>p`00^ZOYD(SOrisHLV0EA79Elw{XP@cc"
    "OnhQ6=@@0;5zTYMJoD9EOGo&Hbd*>*Fr}-GF|%pOG3!BJ@D#Xa@oxkaWW(lM5==cARrv<MIH9)57{eKkAR}nbfBe{EB~KYLknj`I"
    "fZ>3CKolNniu_a@QoEHi5;*9I@8<@X-%hh<ZyA{L_A8m{k!fAD>X1HJ;)1fvxwNB$?Lnsuaf{VcyN7u;>3V~1{zjcst@jQh#`)QI"
    "CS@_HMy|e$nG!~S%3^K^DA;IE7qu8w1EkD@U1f^Y5lMDyTEz3srpQhJ>Olq$MOd^G0M{Ir#VAVo21;;DzA?_4E?&CSrzkYoYxH%e"
    "PzZ39E(!r)Mn$3m(=l2;>dAN>gt9v~>puZigbiBu@(r4xu3z#a0+L3QBcnN}jL1D^$A~h1r#|Y<A!XD;KV4K7A3TD%>q@OLeM;cW"
    "-&mM}5~)(37R%$d0{qblJ$)|R`!J-Tdr_9#?HO>rdZc;3(MD8&cbcSjeGoQgqJrhpl5=F5ipPno{-s3)0gvZ>ZJw$Jr^Cy3nU$J>"
    "GsVWw4Cf>UXjx%+yI_Mygn5C!?U7JV^%*!1jdh6S8PgR$XM$_*wteHzOhZL%f25bKla68tY{HC-IdXJnIX<4o;DrB->aUgeX8sj("
    "MfkN5YQULFB=evBBM#x#XJsQFC~arEXNt&b2Ji?l^{mmfFij}aqT0+Zqw!x!T3K?Oy9{-wCRI&Q7@P&w2-wR8sZ=Rf82m0HK%Mrl"
    "W)Ql~q}UOCtY;PK96gzEg*Xt+2@2RDFgs-<6Bs~jzKH})Qo+Nhh-bfFsnpK2%6?;44<Q&!=2eandk-F$SB6a2Z!<~=(nk<(adW5>"
    "s=v`*0`W?heybx=?bBtKx^)2Xv%Gzp7wFVmZZk@#bO82&3zl#bO(u8oRAw3WzkGw?5471@;wv4+9Q5h@Sas92WljqZ&?RXY>F%NV"
    "Din_ldTqiKOH)y3H9EuneQg)uvCZyoGIBXY%l=sbRjEX}Vb6H^+^c1-%jOgmn4RWI^zF2tvzT-dUSIc(VhW&fm*yJkGEI*u{1VXD"
    "Q+Z}F50Gt?maCQ6O<G5l9$1sWY@9y7YH^v5a0PT_+#-ec%ybB`T1=U1zxI~RG(A&Zfvs>UPejXOW;ip&v0cA0=JrC(?K$dhdkh0O"
    "=ti@6jXARi8RUMXspQI>&-R=De>;e1s8Qj3J@GuGcHQPVHXf3;nOKBqK>gdowIQnC{1Y}N%b2o$8{6y>c8Nz!s~9{QSC_p#60<cQ"
    "QB3H>CYOIG??)ZYLk{e7o6YIm9Ichy-M@dPQL8m3S<ZCspBcFf-5~#8m_zdQ%lF^JuvCk1XWeRC3zegP=^$HnCEe}Q#65}EKyT2c"
    "K@4<s3~x1An`EVNn-kF}yB<>SxA_&G$-g~OzQSkroPqpG&h5!~@QGcJG0zR7n{qc5g75=VSu6=CQ+_#!8DHH$<04r}<~SkdKhsU1"
    "E0ilgcr>Kt@c9#ATF-wb)1UzN?7s9ac}C4<kfigt1OK(jPd0c)$L_h8=ch*aM<Y#3S}*kuaq!9j(l!|El-cji_hUo12Y<PP8;NF`"
    "or#`ZaQ=2T0t{Dc0paRj`?}IT@P%4;oUNXHM}B+U|Mwd@ZKiUO#i7z!RwDx<-P|dE1&9B%yJEo#HRh7vPnj|jfo!DD4@q?Cm2T2_"
    "K86J#<#<wuQW{LRr;wd%Qjt4s{_Y8cXGGdd1ShBG{Ffu6GYHD&Vs=la?W5gV@}pYJpP!|YqJD?FZ1R&I1o0<Ng#vBNXmN^{Q}rP6"
    "h$T9s-SRZf)z6tp0v=_rmdrm5MjJUgv6%iNI&G00(5k#d!$0l*^&Dqzw_P#0H&ahN3uuizCaS_=wNB<pYwG-uSbZQ<y{!^IS5HxZ"
    "Q08~>JehVgVK;sg%gHD*-QrAAIwz(KUlVR<L0Ave{+!AqDs%{XYPVr`|3Z_oEr9KlXStLm6Ums4Mf+iE4QDulsFH9yp;OBl4P<a9"
    "58XP5`vJ=Qi+=lG+KEErOpjHYGs3S0F=O9+=x)`)nORl+>K^Uu_EF-mD6vmfUi2ndTe3RDsERL5e(|u2fbB|W5Itg83uE`_yRqmZ"
    "zeB{BGJIg4QNyD$)$z9P9X|A%t{<I!kYVQe(DadU0oIy!X%QOoD`rfWo%2I)N5XoOdEnFiU#(h`pUd&@Jg!zJexpr?^gA4!(8N$9"
    "g!%P1_e*;6jE9U(o1M%gZqdJhu(>Vn37rHcgJceg@{%JXLfm``;#)eSjZo36m3qAYhT`rSo4`Cbo$E93=8&S}+{_(6k(iE~$rpOk"
    "k2F@J=tH9p%rc2t_6W^HI%*uDvc-(;?&D9+IT{Zv%xoEhz<(h|>O}tv<oQnn(fr8_6hr-!YRQ5SyXpgl8H`J+tsz5-n5pO)u&Wmn"
    ")h<}pBIVEcPfm#3Vlix9C}y$nVf*`$(19-doH+lMP|y`UjQK&&S<R1g9gg7T`oPK6Kcs?GRfE3El3|$qE(7!QdN;t9{{acu6v+"
)
VALUES = {c: i for i, c in enumerate("23456789TJQKA", start=2)}


def rank(hand):
    vals = sorted((VALUES[card[0]] for card in hand), reverse=True)
    cnt = Counter(vals)
    groups = sorted(((m, v) for v, m in cnt.items()), reverse=True)
    straight = len(cnt) == 5 and vals[0] - vals[-1] == 4
    flush = len({card[1] for card in hand}) == 1

    if straight and flush:
        return 8, vals[0]
    if groups[0][0] == 4:
        return 7, groups[0][1], groups[1][1]
    if groups[0][0] == 3 and groups[1][0] == 2:
        return 6, groups[0][1], groups[1][1]
    if flush:
        return 5, *vals
    if straight:
        return 4, vals[0]
    if groups[0][0] == 3:
        rest = sorted((v for v, m in cnt.items() if m == 1), reverse=True)
        return 3, groups[0][1], *rest
    if groups[0][0] == groups[1][0] == 2:
        pairs = sorted((v for v, m in cnt.items() if m == 2), reverse=True)
        rest = next(v for v, m in cnt.items() if m == 1)
        return 2, *pairs, rest
    if groups[0][0] == 2:
        rest = sorted((v for v, m in cnt.items() if m == 1), reverse=True)
        return 1, groups[0][1], *rest
    return 0, *vals


def solve():
    text = decompress(b85decode(DATA)).decode()
    return sum(
        rank(cards[:5]) > rank(cards[5:])
        for cards in (line.split() for line in text.splitlines())
    )


if __name__ == "__main__":
    print(solve())