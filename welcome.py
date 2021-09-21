import emoji
from ansi.colour import fg


def logo():
    print(
        fg.brightgreen(f"""
__        ___    ____     _
\ \      / / \  |  _ \ __| | ___ _ __
 \ \ /\ / / _ \ | |_) / _` |/ _ \ '_  |
  \ V  V / ___ \|  _ < (_| |  __/ | | |
   \_/\_/_/   \_\_| \_\__,_|\___|_| |_|"""))
    print("")
    print(
        emoji.emojize(
            "     Node Edition :key:"))


def goodbye():
    for n in range(0, 300):
        print("")
        
    print(fg.yellow("""
                 ,.=ctE55ttt553tzs.,                               
             ,,c5;z==!!::::  .::7:==it3>.,                         
          ,xC;z!::::::    ::::::::::::!=c33x,                      
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.                    
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.                  
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.                
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     \itL               
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk              
 .EJ.    ;::::::L                   "\:.   ::.    Jttl             
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L            
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3            
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13
E:.    !::::::::::::L               =Et::::::::!  ::|13   
E:.    !::::::::::::L    .......       \:::::::!  ::|i3   
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13   
!:.     .:::::    ::L    |t::::::3L     |:::::; ::::EE3   
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[            
 Jt1.    :::::::[                    ;z5::::;.::::;3t3             
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L             
   \i3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L              
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`               
      \z3.       ::;:::::::::::::::;='      ./355F                 
        \z3x.         ::~======='         ,c253F                   
          "tz3=.                      ..c5t32^                     
             "=zz3==...         ...=t3z13P^                        
                 `*=zjzczIIII3zzztE3>*^`   """))
    
    
def umbrel():
    return (fg.magenta("""
              ,;###GGGGGGGGGGl#Sp
           ,##GGGlW""^'  '`""%GGGG#S,
         ,#GGG"                  "lGG#o
        #GGl^                      '$GG#
      ,#GGb                          GGG,
      lGG"                            "GGG
     #GGGlGGGl##p,,p##lGGl##p,,p###ll##GGGG
    !GGGlW''''''*GGGGGGG#'WlGGGGG#W''*WGGGGS
     ''          '^          ''          ''
                @GGS         lG#
                !GGG        !GGG
                !GGG        !GGG
                !GGG        !GGG
                !GGG        !GGG
                !GGG        !GGG
                'GGG        $GGl
                 "GGG#psqp##GG#
                   "%GGGGGG# """))
