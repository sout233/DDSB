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
    "我看见一个蹦蹦跳跳的女......"
    "煞笔"
    "在向我招着手。"
    "她是我的青梅竹马，至少设定上是这样。"
    "本来是打算七点就去上学的，但最近的上学时间却总是被她睡懒觉的时间所耽误。"
    "真是麻烦啊……"
    "但我还是停了下来……"
    show sayori 4p zorder 2 at t11
    s "哈...哈..."
    mc "你再睡下去我们就该迟到了。"
    s "抱歉抱歉..."
    mc "勉强...原谅你吧..."
    s "嘿嘿，我就知道。"
    mc "……"
    s "啊对了…"
    mc "？"
    show sayori 5e
    s "那个…"
    mc "？？"
    s "嗯……"
    mc "？？？"
    s "……"
    mc "有话快说。"
    s "嘤嘤嘤"
    s "我说出来你别打我哈。"
    mc "行。"
    "虽然感觉有点怪怪的"
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
    show sayori 4p at t11
    s "呜呜……"

menu:
    "安慰她":
        jump apologize_line
    "直接去上学":
        jump direct_school_line

return 

label direct_school_line:
    mc "快去上学。"
    show sayori 1r
    s "你妈的，啰里啰唆。"
    s "快他妈去上学。"
    mc "啊这…刑吧"
    show sayori 2c
    s "啥？"
    show sayori 1c
    s "……"
    jump school_start

label apologize_line:
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
    show sayori at lhide
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
    s 2e "nmd，你没听见好吧。"
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
    show sayori 1b at t11
    s "那你帮我收拾收拾呗。"
    mc "我不每天都帮你收拾吗，你却总能在三分钟内恢复原样。"
    s 3 "嘿嘿…"
    s 3c "啊啦，先不说这个了。"
    s 1b "诺，二维码。"
    mc "唔，行。"
    mc "等下我手机呢？"
    "我翻遍了我的口袋，却找不到手机"
    mc "完了，手机没了。"
    s "啊这，你好好想想是不是掉哪了。"
    mc "我想想…"
    mc "哦对！你吓我的时候，手机从口袋里掉了出来！"
    s "？"
    show sayori 4h at s11
    s "你骗人，我看的清清楚楚，根本没有。"
    mc "你没事老乱看干嘛啊。"
    s 1i "因为我喜欢。"
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
    show sayori 3j zorder 2 at t11
    s "可你的不是P40吗？"
    mc "啊这，你就当它是友商的机子就行了。"
    s "那我嫉妒，然后呢？"
    mc "然后你就把它偷了。"
    jump iss_isfrend_line

label iss_wanna_peep_line:
    mc "也许你是想查我手机？"
    show sayori 5d 
    s "啊这…"
    s "当然我想…但我不会这么做。"
    stop music fadeout 2.0
    play music t3
    jump not_sayori_line

label iss_wanna_steal_line:
    mc "因为你想盗刷我信用卡！"
    s "你有信用卡吗？"
    mc "啊这，那就偷我微信里的钱…"
    s "你微信里有多少钱？"
    mc "em…大概…0.9元……"
    s "那我有偷你的必要吗？"
    mc "反正你就是偷了。"
    jump iss_isfrend_line

label iss_isfrend_line:
    s "你就这样主观臆断。"
    show sayori 1d zorder 2 at s11
    "纱世里摇了摇头，嘴角透出一丝无奈的笑容。"
    s "你不记得你压根就没带手机吗？"
    stop music fadeout 2.0
    play music t3
    mc "啊这…"
    "好像也是……"
    "我突然发觉我现在的处境很尴尬。"
    show sayori 1g
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
        stop music fadeout 3.0
        pause 3.0
        play music td
        s ""
        return
    "不是":
        mc "不是。"
        s "那好吧…"
        s ""
        s ""
        s ""
        s "快走"
        show sayori zorder 1 at thide
        hide sayori
        s ""
menu:
    "走":
        s ""
        ""
        "纱ÅÆÇ…"
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

label dev_fakebug_line:
    mc "真相只有一个！"
    play music "audio/kn_sax.mp3"
    sayori "？"

label not_sayori_line:
    mc "所以说我应该是落在哪里了。"
    show sayori 1c zorder 2 at t11
    s "说就是嘛…"
    s "不过，你是不是压根就没带？"
    mc "啊是！"
    mc "我糊涂了。"
    s 2x "啊哈哈哈哈。"
    "我觉得纱世里貌似并不是很在意。"
    s 1b "那么赶紧回你家拿去。"
    mc "唔…好"
    "我在考虑要不要让纱世里陪着去。"
    mc "不如你陪我一起去？"
    show sayori 4r at s11
    s "我很乐意！"
    mc "那快走吧。"

label sy_wentmcroom_line:
    scene bg bedroom
    with wipeleft_scene
    show sayori 1a zorder 2 at t11
    s "哈，好久没来你房间了。"
    mc "好久？"
    show sayori glitch
    s "啊这……"
    s "唔…有点头疼"
    mc "没事吧？"
    show sayori 1t zorder 2
    s "没事，好点了。"
    s 1d"你手机呢？"
    mc "唔…在桌子上！"
    "我从桌子上拿起了手机。"
    $ renpy.call_screen("dialog", message="你拿起了手机\naGVscCBtb25pa2E=", ok_action=Return())
    "感觉有种电流通过了我的身体，难不成是手机漏电了？"
    s 2c "你愣着干嘛呢？"
    mc "啊啊，抱歉。"
    s 1c "等我找下二维码…"
    s 1b "诺，这个。"
    image help_me_QR_Code = im.Composite((250, 500), (0, 0), "images/monika/help_me.png")
    show sayori zorder 1 at thide
    hide sayori
    show dark:
        alpha 0.6
    show help_me_QR_Code zorder 1
    pause 2.0
    s "扫完了吗？"
    mc "嗯…"
    show help_me_QR_Code zorder 1 at thide
    hide help_me_QR_Code
    show dark zorder 1 at thide
    hide dark
    show sayori 2b zorder 2 at s11
    mc "让我点下加入…" 
    $ renpy.call_screen("dialog", message="你加入了群聊\"屑文艺交流群\".\naGVscCBtb25pa2E=", ok_action=Return())
    mc "什么…文艺？"
    s 2a "嘿嘿，我的意思是，你的文化课不好，我觉得你需要补课了。"
    mc "你当初可不是这么说的。"
    s 1b "我是怎么说的？"
    mc "浴室…"
    s 4b "笨蛋，那是在骗你。"
    mc "这是无用功，你以为你拉我进了这个群我的文化课成绩就能提高吗？"
    s 1c "那可说不定。"
    s "你还说我呢，我的成绩都比你好！"
    mc "可你数学分数比我低。"
    s 5d "咳咳，现在在说文科…文科。"
    mc "我承认我文科差了点，不过你打算怎么帮我？"
    s 2c "呐，这个群。"
    mc "这个群？"
    mc "有什么用？"
    s "群里除了我以外，还有另外两个人，她们会帮你的。"
    mc "两个人？"
    s "对的，而且她们都是女孩子。"
    "{cps=50}我突然有点性趣………………{/cps}{nw}"
    "我突然有点兴趣了，当然不能被纱世里看出来（）"
    mc "我知道了，所以说，她们该怎么帮我？"
    s 1b "她们会给你发题目的。"
    mc "题目？"
    s "就是简单的测试题而已。"
    "我不禁觉得什么美女老师在线发题，也许是真的。"
    mc "语文相关的吗？"
    s "是的，主要是诗，有时候还会夹杂点作文。"
    mc "希望不会太难…"
    s "放心，不会的。"
    s 1c "如果你想的话，现在就可以试试。"
    mc "啊这？"
    s 3b "她们发题了……"
    s 1b "要做吗？"
    mc "做吧…"
    s "刑。"
    mc "什么谐音梗。"
    s 1a "嘻嘻。"
    s "手机给你。"
    show sayori 4r at h11
    s "加油！"
    call poem from _call_poem
    scene bg bedroom
    with dissolve
    show sayori 1a zorder 2 at t11
    play music t3
    s "怎么样？"
    mc "还行，写诗可太草了。"
    s 2a "啊哈，这是我们的风格。"
    mc "神tm风格"
    s "嗯哼，你会习惯的。"
    s 1c "相比这个，我们每天放学的时候都会在活动室见面。"
    mc "线下见面？而且还是在学校的活动室？"
    s 1b"emm…说是线下见面的话，倒不如说是聚会了。"
    mc "怎么说？"
    s "她们和我们是在同一个学校。"
    mc "啊这？"
    mc "那…同一个年级吗？"
    s "哦不，有两个比我们小。"
    "我有学妹了，好耶！"
    "不行，蛋定。"
    mc "咳咳，所以接下来？"
    s 2c "你没事搭什么腔啊。接下来，接下来我该问你了。"
    s 1c "你要不要跟着我去？"
    mc "嗯？去干嘛。"
    s "见面？"
    mc "\"线下见面？\""
    s 1b "\"聚会\""
    "好机会wwwwwwwwwwwwwww"
    mc "嗯…容我考虑考虑…"
    "欸嘿嘿嘿，这波啊，这波不仅有妹子一对一指导，而且还能见面！"
    "生活如此美好，妹子如此多娇。"
    "不愧是我[player]！能有今天我要感谢我的父母，以及我的老师，同学还有亲人…"
    show sayori 2c at h11
    s "想好了吗？"
    mc "啊…啊……"
    mc "想好了！"
    s 1a "那刑吧，明天下午记得等我。"
    mc "你又要去我教室吗？"
    s "嗯哼。"
    mc "那可别在像上次那样吓我了。"
    s 2x "嘿嘿，说不定呢。"
    mc "NMLGB"
    mc "我感觉我班里的同学又开始议论纷纷了。"
    s 1b "议论什么？"
    mc "就那些\'磕学家\'，貌似在磕我们的cp"
    s 3b "所以…为什么？"
    mc "我哪知道她们…"
    s 1a "噗，那不是挺好玩的吗。"
    mc "等你真听见了就不会觉得好玩了。"
    s "啊啦，没关系，反正隐隐约约有一点…"
    mc "唔……什么？"
    show sayori 2y at h11
    s "啊没事。"
    s 2b "唔，时间不早了…"
    s 1b "我得回去了。"
    mc "啊好吧，那…明天见？"
    s "明天见。"
    mc "嗯，拜拜。"
    show sayori zorder 1 at thide
    hide sayori
    "我得好好看看这个奇怪的群…"
    "说不定这是我学校生涯中爱情的开始？"
    "欸嘿嘿嘿…"
    show sayori 2b zorder 2 at t11
    s "欸对了…"
    mc "草你又吓我。"
    s 4p "嘤，不是。"
    s 5c "我是想提醒你…记得每天晚上做这个题。"
    mc "唔，好吧。"
    mc "快走吧，路上小心。"
    s 2a "那拜咯~"
    show sayori zorder 1 at thide
    hide sayori
    mc "拜拜。"
    "时间雀食不早了，我也得睡觉了玛德。"
    scene black
    with dissolve
    pause 2.0
    "明天貌似还有个考试。"
    "也可以说是测验吧…"
    "不管那么多了，养足精神最重要！"
    "唔……"
    pause 2.0
    "……呼噜噜"
    pause 3.0
    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "[player]?.."
    s 1g "..."
    s "这..."
    s "这什么东西...?"
    s "哦不..."
    s 1u "不..."
    s "草。"
    s "不应该这样的。"
    s 4w "What is this?"
    s "What am I?"
    s "Make it stop!"
    s "PLEASE MAKE IT STOP!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return

#终于写完第一章了耶！
