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
    for n in range(0, 100):
        print("")
        
    print(fg.magenta("""
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
    print("")                   
    print(fg.magenta("                   www.getumbrel.com"))
    print("")
    
    
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
