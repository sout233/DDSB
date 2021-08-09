label ch1_start:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "等等我！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"
    mc "？"
    mc "你吼那么大声干嘛啊"
    "我看见一个蹦蹦跳跳的女......"
    "煞笔"
    "在向我招着手。"
    "她是我的青梅竹马，至少设定上是这样。"
    "本来爷是打算七点就去上学的，但最近的上学时间却总是被她睡懒觉的时间所耽误。"
    "你可能理解不了，就……挺jb怪的。"
    "相处时间久了，自然就会这样。"
    "虽然她着急忙慌跑过来的亚子搞得我尬死了"
    "但我还是停了下来……"
    show sayori 4p zorder 2 at t11
    s "哈...哈..."
    mc "你再睡下去咱俩估计就得挨批了"
    s "抱歉抱歉"
    s "啊对了…"
    mc "？"
    show sayori 5e
    s "那个…"
    mc "？？"
    s "嗯……"
    mc "？？？"
    s "……"
    mc "你踏马有话快说。"
    s "嘤嘤嘤（"
    s "我说出来你别打我哈。"
    mc "刑"
    s "能不能…给我点涩图，我梯子上不去了"
    play sound "sfx/smack.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 2p at h11
    "{i}pia~{/i}"
    s "哼哼哼啊啊啊啊！！"
    show sayori 3g at s11
    s "你不是说不打我的吗。"
    mc "我说的\"刑\"，刑法的刑"
    show sayori 4p at t11
    s "谐音梗！扣钱！"

menu:
    "介绍刑法":
        jump xing_start
    "去上学":
        jump GotoSchool_start

return

label xing_start:
    mc "《中华人民共和国刑法》是为了惩罚犯罪，保护人民，根据宪法，结合我国同犯罪作斗争的具体经验及实际情况，制定的法律。刑法的任务，是用刑罚同一切犯罪行为作斗争，以保卫国家安全，保卫人民民主专政的政权和社会主义制度，保护国有财产和劳动群众集体所有的财产，保护公民私人所有的财产，保护公民的人身权利、民主权利和其他权利，维护社会秩序、经济秩序，保障社会主义建设事业的顺利进行。《中华人民共和国刑法》由中华人民共和国第五届全国人民代表大会第二次会议于1979年7月1日通过，自1980年1月1日起施行。最新修订是由中华人民共和国第八届全国人民代表大会第五次会议于1997年3月14日修订，自1997年10月1日起施行。"
    s "你妈的，啰里啰唆。"
    s "快他妈去上学。"
    mc "啊这…刑吧"
    s "啥？"
    mc "我说行，银行的行。"
    s "emmm…貌似也对，管他呢，gkd。"

    jump school_start

label GotoSchool_start:
    mc "汗，我错了行吧。快去上学去。"
    s "啧，那就…原谅你吧，就这一次。"
    mc "嘻"
    s "快走！"
    
    jump school_start

label school_start:
    mc "到了"

    

