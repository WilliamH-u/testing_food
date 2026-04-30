import numpy as np
max_height = 10 #height of tallest letters

letter = {
    "A":[
        ("down",),
        ("line", max_height/6, max_height/2,),
        ("line", max_height/3, 0,),
        ("line", -max_height/3, 0,),
        ("line", max_height/6, max_height/2,),
        ("line", max_height/3, -max_height,),
        ("up",),

    ],
    
    "B": [("down",),
          ("line", 0, max_height,),
          ("line", max_height/5, 0,),
          ("cw", 0, -max_height/2, 0, -max_height/4 ),
          ("line", -max_height/5, 0,),
          ("line", max_height/5, 0,),
          ("cw", 0, -max_height/2, 0, -max_height/4 ),
          ("line", -max_height/5, 0,),
          ("up",),
          ("line", 9*max_height/20, 0,),

          ],
    "C": [
        ("line", max_height/2, max_height/4,),
        ("down",),
        ("cw", -max_height/2, 0, -max_height/4, 0 ),
        ("line", 0, max_height/2,),
        ("cw", max_height/2, 0, max_height/4, 0 ),
        ("up",),
        ("line", 0, -3*max_height/4,),
        
    ],
    "D":[
        ("down",),
        ("line", 0, max_height,),
        ("cw", 0, -max_height, 0, -max_height/2 ),
        ("up",),
        ("line", max_height/2, 0,),

    ],


    "E":[("down",),
         ("line", 0, max_height,),
         ("line", max_height/2, 0, ),
         ("up",),
         ("line", 0, -max_height/2,),
         ("down",),
         ("line", -max_height/2, 0, ),
         ("line", 0, -max_height/2,),
         ("line", max_height/2, 0, ),
         ("up",),

         ],

    "F":[("down",),
         ("line", 0, max_height,),
         ("line", max_height/2, 0, ),
         ("up",),
         ("line", 0, -2*max_height/5,),
         ("down",),
         ("line", -max_height/2, 0, ),
         ("up",),
         ("line", max_height/2, -3*max_height/5,),
        ],
    
    "G":[
        ("line", max_height*(1/2 + np.sqrt(2)/4), max_height*(1/2 + np.sqrt(2)/4),),
        ("down",),
        ("ccw", max_height*(1/2-(np.sqrt(2)/4)), -max_height*(np.sqrt(2)/4), -max_height*(np.sqrt(2)/4), -max_height*(np.sqrt(2)/4)),
        ("line", -max_height/2, 0, ),
        ("up",),
        ("line", max_height/2, -max_height/2, ),

    ],


    "H":[
        ("down",),
         ("line", 0, max_height,),
         ("line", 0, -max_height/2,),
         ("line", max_height/2, 0,),
         ("line", 0, max_height/2,),
         ("line", 0, -max_height,),
         ("up",),

        ],

    "I":[
        ("line", 0, max_height,),
        ("down",),
        ("line", max_height/2, 0, ),
        ("line", -max_height/4, 0, ),
        ("line", 0, -max_height,),
        ("line", -max_height/4, 0, ),
        ("line", max_height/2, 0, ),
        ("up",),

    ],

    "J":[
        ("line", 0, max_height/4,),
        ("down",),
        ("ccw", max_height/2, 0, max_height/4, 0 ),
        ("line", 0, 3*max_height/4,),
        ("line", -max_height/6, 0,),
        ("line", max_height/3, 0,),
        ("up",),
        ("line", 0, -max_height,),

    ],

    "K":[
        ("down",),
        ("line", 0, max_height,),
        ("up",),
        ("line", max_height/2, 0,),
        ("down",),
        ("line", -max_height/2, -max_height/2,),
        ("line", max_height/2, -max_height/2,),
        ("up",),

    ],

    "L": [("line", 0, max_height,),
          ("down",),
          ("line", 0, -max_height,),
          ("line", max_height/2, 0,),
          ("up",),


          ],
    
    "M":[
        ("down",),
        ("line", 0, max_height,),
        ("line", 2*max_height/5, -max_height,),
        ("line", 2*max_height/5, max_height,),
        ("line", 0, -max_height,),
        ("up",),

    ],

    "N":[
        ("down",),
        ("line", 0, max_height,),
        ("line", 2*max_height/3, -max_height,),
        ("line", 0, max_height,),
        ("up",),
        ("line", 0, -max_height,),

    ],
    
    "O": [("line", 9*max_height/20, 0,),
          ("down",),
          ("cw", -9*max_height/20, 9*max_height/20, 0, 9*max_height/20 ),
          ("line", 0,2*max_height/20 ),
          ("cw", 18*max_height/20, 0,  9*max_height/20, 0 ),
          ("line", 0,-2*max_height/20 ),
          ("cw", -9*max_height/20, -9*max_height/20, -9*max_height/20, 0 ),
          ("up",),
          ("line", 9*max_height/20, 0,),

           ],
    
    "P":[
        ("down",),
        ("line", 0, max_height,),
        ("line", max_height/4, 0,),
        ("cw", 0, -max_height/2, 0, -max_height/4 ),
        ("line", -max_height/4, 0,),
        ("up",),
        ("line", max_height/2, -max_height/2,),

    ],

    "Q":[
        ("line", 9*max_height/20, 0,),
        ("down",),
        ("cw", -9*max_height/20, 9*max_height/20, 0, 9*max_height/20 ),
        ("line", 0,2*max_height/20 ),
        ("cw", 18*max_height/20, 0,  9*max_height/20, 0 ),
        ("line", 0,-2*max_height/20 ),
        ("cw", -9*max_height/20, -9*max_height/20, -9*max_height/20, 0 ),
        ("up",),
        ("line", 0, 6*max_height/20,),
        ("down",),
        ("line", 9*max_height/20, -6*max_height/20,),
        ("up",),
    ],

    "R":[
        ("down",),
        ("line", 0, max_height,),
        ("line", max_height/4, 0,),
        ("cw", 0, -max_height/2, 0, -max_height/4 ),
        ("line", -max_height/4, 0,),
        ("line", max_height/2, -max_height/2,),
        ("up",),

    ],

    "S":[
        ("line", (max_height/4)*(1 - np.sqrt(2)/2), (max_height/4)*(1 - np.sqrt(2)/2),),
        ("down",),
        ("ccw", (max_height/4)*(np.sqrt(2)/2), (max_height/4)*(1+np.sqrt(2)/2), (max_height/4)*(np.sqrt(2)/2), (max_height/4)*(np.sqrt(2)/2)),
        ("cw", (max_height/4)*(np.sqrt(2)/2), (max_height/4)*(1+np.sqrt(2)/2), 0, max_height/4,),
        ("up",),
        ("line", (max_height/4)*(1 - np.sqrt(2)/2), -(max_height/4)*(3 + np.sqrt(2)/2),),

    ],

    "T":[
        ("line", 0, max_height,),
        ("down",),
        ("line", 3*max_height/4, 0,),
        ("line", -3*max_height/8, 0,),
        ("line", 0, -max_height,),
        ("up",),
        ("line", 3*max_height/8, 0,),

    ],

    "U":[
        ("line", 0, max_height,),
        ("down",),
        ("line", 0, -2*max_height/3,),
        ("ccw", 2*max_height/3, 0, max_height/3, 0, ),
        ("line", 0, 2*max_height/3,),
        ("up",),
        ("line", 0, -max_height,),

    ],

    "V":[
        ("line", 0, max_height,),
        ("down",),
        ("line", max_height/3, -max_height,),
        ("line", max_height/3, max_height,),
        ("up",),
        ("line", 0, -max_height,),

    ],

    "W":[
        ("line", 0, max_height,),
        ("down",),
        ("line", max_height/5, -max_height,),
        ("line", max_height/5, max_height,),
        ("line", max_height/5, -max_height,),
        ("line", max_height/5, max_height,),
        ("up",),
        ("line", 0, -max_height,),

    ],

    "X":[
        ("down",),
        ("line", 2*max_height/3, max_height,),
        ("up",),
        ("line", -2*max_height/3, 0,),
        ("down",),
        ("line", 2*max_height/3, -max_height,),
        ("up",),

    ],

    "Y":[
        ("line", max_height/3, 0,),
        ("down",),
        ("line", 0, max_height/2,),
        ("line", -max_height/3, max_height/2,),
        ("line", max_height/3, -max_height/2,),
        ("line", max_height/3, max_height/2,),
        ("up",),
        ("line", 0, -max_height,),
        
    ],

    "Z":[
        ("line", 0, max_height,),
        ("down",),
        ("line", 2*max_height/3, 0,),
        ("line", -2*max_height/3, -max_height,),
        ("line", 2*max_height/3, 0,),
        ("up",),

    ],

    " ":[
        ("line", max_height/3, 0,),

    ],




}


