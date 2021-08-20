#一周目
#——————
#第一幕
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
    show yuri eyesfull at t11
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
        jump xing_line
    "去上学":
        jump GotoSchool_line

return 

label xing_line:
    mc "《中华人民共和国刑法》是为了惩罚犯罪，保护人民，根据宪法，结合我国同犯罪作斗争的具体经验及实际情况，制定的法律。刑法的任务，是用刑罚同一切犯罪行为作斗争，以保卫国家安全，保卫人民民主专政的政权和社会主义制度，保护国有财产和劳动群众集体所有的财产，保护公民私人所有的财产，保护公民的人身权利、民主权利和其他权利，维护社会秩序、经济秩序，保障社会主义建设事业的顺利进行。《中华人民共和国刑法》由中华人民共和国第五届全国人民代表大会第二次会议于1979年7月1日通过，自1980年1月1日起施行。最新修订是由中华人民共和国第八届全国人民代表大会第五次会议于1997年3月14日修订，自1997年10月1日起施行。"
    show sayori 1r
    s "你妈的，啰里啰唆。"
    s "快他妈去上学。"
    mc "啊这…刑吧"
    show sayori 2c
    s "啥？"
    mc "我说行，银行的行。"
    show sayori 1c
    s "emmm…貌似也对，管他呢，gkd。"
    jump school_start

label GotoSchool_line:
    mc "汗，我错了行吧。快去上学去。"
    show sayori 1b
    s "啧，那就…原谅你吧，就这一次。"
    mc "嘻"
    show sayori at h11
    s "快走！"
    jump school_start

#第二幕

label school_start:
    scene corridor with dissolve_scene_full
    mc "还有一分钟…还好赶到了…"
    show sayori 1b zorder 2 at t11
    s "欸莫得事，老师就是个逊啦。"
    show sayori 1d
    mc "上次你上课打音游，老师过来你他妈吓得跟个蔡虚坤似的。"
    show sayori at s11
    s "嘤。话说…"
    show sayori 1c
    s "你要不要加我那个群"
    mc "啥群"
    s "文……"
    mc "不加"
    s "文艺少女浴室写真流出"
    mc "我加！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"
    show sayori 2b at h11
    s "你吼那么大声干嘛啊"
    mc "欸嘿嘿"
    show sayori 1b
    s "那就放学的时候，来我家里，我家还蛮大的。"
    mc "唔…"

menu:
    "然后呢？":
        jump thenwhat_line
    "登dua郎？":
        jump dua_line

label thenwhat_line:
    mc "然后呢？"
    s "然后，我会给你个二维码，你扫就刑了。"
    mc "就这？"
    s "对，不然呢？"
    mc "那你不能现在给吗？"
    show sayori 1c
    s "你丫的以为教育法白给的吗，要能带手机我早给你了。"
    mc "太逊了。"
    s "难不成你带了？"
    mc "没。"
    show sayori 1a at t11
    s "太逊了，啧啧啧。"
    s "那就这么说定了，放学你来我家。"
    mc "好好好，快去教室。"
    hide sayori
    "纱世里一溜烟的跑走了。"
    "我一边生怕她会摔倒，一边一步步挪到了教室门口。"
    jump thinking_start

label dua_line:
    mc "去你家？怎么，登dua郎吗"
    s 2p "笨蛋，我是叫你去我家加群。到时候我会给你二维码的。"
    show sayori 5h
    s "当然你想登dua郎也不是不行……"
    mc "？"
    s 2e "你妈的，你没听见好吧。"
    mc "那我没听见就没听见吧。"
    show sayori 1b
    s "嘁，那就这么说定了啊。"
    mc "刑"
    s "别忘了，快去教室吧。"
    hide sayori at t21
    "……"
    "望着纱世里的背影…总感觉做错了什么。"
    "我转身走进教室。"
    jump thinking_start

#第三幕

label thinking_start:
    play music t3
    scene black 
    with wipeleft_scene
    "已经上了一下午的课了"
    pause 3.0
    "(放学铃)"
    mc "啊啦啊啦，终于放学了。"
    "(叮呤呤呤呤呤呤呤呤呤呤呤)"
    mc "不知道纱世里给我的群里有什么好东西。"
    "(叮呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤)"
    mc "难不成是什么学习资料？"
    "(叮呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤呤)"
    mc "欸嘿嘿嘿……"
    "\"你是伞兵吗[player]，电话响了都不接\""
    mc "啊…哦哦哦抱歉"
    mc "尬死了……"
    mc "唔…是纱世里打来的"
    "我接起电话并走到了走廊"
    pause 1.0
    scene bg corridor 
    with wipeleft_scene
    mc "喂？"
    s "你是睡着了吗？"
    mc "才没有…"
    s "嘿嘿。"
    s "怎么，你现在在哪？"
    mc "唔，我在我教室后门外。"
    s "欸？"
    mc "怎么了？"
    s "啊，没事…"
    mc "你是要来找我吗？"
    mc "我说，那样可不太好，万一被误认成情侣就麻烦了。"
    s "……"
    mc "你说是吧"
    mc "纱世里？"
    mc "？"
    scene black
    "有人盖住了我的双眼。"
    mc "谁？"
    "\"……\""
    pause 3.0
    scene bg corridor
    mc "怎么……"
    show sayori 1b at face
    mc "哇啊啊啊啊啊啊啊啊啊啊！！！"
    show sayori 1a at t11
    s "哈！太逊了"
    mc "你麻痹的，差点没把老子吓死！"
    show sayori 4r
    s "欸嘿嘿嘿…"
    s "行了快走吧。"
    mc "啊…好"
    scene black
    with wipeleft_scene
    "我总感觉有人在看着我。"
    scene bg house
    with dissolve
    s "到了，是不是已经迫不及待了？"
    mc "你才迫不及待呢。"
    s "的确是呢…"
    mc "？"
    s "诶呀快上去。"
    mc "唔…"
    scene bg sayori_bedroom
    with fade
    mc "还是一如既往的乱呐…"
    s "那你帮我收拾收拾呗。"
    mc "我不每天都帮你收拾吗，你却总能在三分钟内恢复原样。"
    s "嘿嘿…"
    s "啊啦，先不说这个了。"
    s "诺，二维码。"
    mc "唔，行。"
    mc "等下我手机呢？"
    "我翻遍了我的口袋，却找不到手机"
    mc "完了，手机没了。"
    s "啊这，你好好想想是不是掉哪了。"
    mc "我想想…"
    mc "哦对！你吓我的时候，手机从口袋里掉了出来！"
    s "？"
    s "你骗人，我看的清清楚楚，根本没有。"
    mc "你没事老乱看干嘛啊。"
    s "因为我喜欢。"
    mc "所以说……"

menu:
    "是纱世里干的":
        jump is_sayori_line
    "不是纱世里干的":
        jump not_sayori_line
    "开发者干的":
        jump dev_fakebug_line

label is_sayori_line:
    mc "真相只有一个！"
    play music "audio/kn_sax.mp3"
    s "？"
    mc "是你偷走了我的手机！"
    s "等会我为什么要偷…"
    mc "因为你…"

menu:
    "嫉妒我机子贵":
        jump iss_phone_expensive_line
    "想偷钱":
        jump iss_wanna_steal_line
    "想查我手机":
        jump iss_wanna_peep_line

label iss_phone_expensive_line:
    mc "因为你嫉妒我的小米MIX4贵！"
    s "可你的不是P40吗。"
    mc "啊这，你就当它是友商的机子就行了。"
    s "那我嫉妒，然后呢？"
    mc "然后你就把它偷了。"
    s "你就这样主观臆断。"
    "纱世里摇了摇头，嘴角透出一丝无奈的笑容。"
    s "你不记得你压根就没带手机吗？"
    stop music fadeout 2.0
    play music t3
    mc "啊这…"
    "好像也是……"
    "我突然发觉我现在的处境很尴尬。"
    s "你好心带你来我家，本来还想给你看点好东西…"
    s "可你就这么对我。"
    s "快走吧。"
    mc "可是…"
    s "别说了，我们一直都是好朋友对吧…"

menu:
    "是":
        mc "是的…"
        s "那你快回家吧…看看你的手机还在不在。"
        mc "好吧。"
        "我无奈的转过了身，推门而出。"
        scene bg house
        with dissolve
        "我向上望了望纱世里的窗户。"
        "什么都没看见。"
        "……"
        stop music fadeout 3.0
        pause 3.0
        play music t3g3
        mc "等会…怎么突然有点头晕……"
        show dark:
            alpha 0.6
        "我意识到事情不太对。"
        mc "纱世里！"
        mc "纱世里！！救救我！"
        "（无人应答）"
        show darkred:
            alpha 0.6
        with fade
        mc "纱……"
        "……"
        s ""
        return
    "不是":
        mc "不是。"
        s "那好吧…"
        s ""
        s ""
        s ""
        s "快走"
        s ""
menu:
    "走":
        s ""
        ""
        mc "纱ÅÆÇ…"
        "我离开了纱世里的家"
        scene bg house
        "……"
        show dark:
            alpha 0.6
        "……"
        pause 3.0
        show sayori glitch
        pause 1.0
        return


label not_sayori_line:

label dev_fakebug_line:
    mc "真相只有一个！"
    play music "audio/kn_sax.mp3"
    sayori "？"
