#一周目
#——————
#第二幕
label ch2_start:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    
    "\"太阳当空照~花儿对我笑~\""
    mc "今天可真是个好日子。"
    mc "等会今天貌似要考试…"
    mc "什么破日子！糟透了！"
    mc "不过我得先去找纱世里…"
    scene bg house
    with wipeleft_scene
    mc "阳光明媚…"
    mc "……"
    mc "cun意盎然。"
    mc "纱世里估计还在睡觉吧。"
    "我从兜里掏出了钥匙，打开了纱世里家的门…"
    scene black
    with dissolve_scene_full
    "房门虚掩着…"
    mc "直接进去貌似不太好吧…"
    mc "纱世里！"
    mc "再不起来太阳都晒屁股了。"
    mc "纱世里？"
    "睡得那么死……不愧是她。"
    mc "再不起来我就进来了哦。"
    "看来得进去看看了。"
    "我轻轻地推开了门……"
    scene bg sayori_bedroom
    with dissolve_scene_full
    mc "……"
    mc "纱世里…？"
    mc "她不可能走那么早吧…"
    show sayori 4r zorder 2 at face
    s "哈！"
    show sayori 1a zorder 2 at t11
    mc "草！"
    mc "你又吓我！"
    s 4c "呜呜，我不是故意的…"
    mc "那我刚才叫你你怎么不出声？"
    s 1b "那是因为…我刚才在戴着耳机。"
    mc "你还会听歌？"
    s 4b "那，当然。"
    mc "什么类型的？"
    s 1b "钢琴曲…"
    mc "没想到你的品味最近有进步了。"
    s "搞得我品味一直不怎么样似的。"
    mc "马马虎虎吧。"
    s "嘁。"
    mc "快走吧，又得迟到了。"
    s 1c "啊行。"
    show sayori zorder 1 at thide
    hide sayori
    scene black
    with pushright
    mc "唔……又是无聊的一天。"
    mc "都五点了还拖堂，麻痹的。"
    pause 3.0
    "……"
    "下课了。"
    mc "说下课就下课了。"
    mc "我得先给纱世里打个电话。"
    scene bg corridor
    with wipeleft
    mc "歪歪歪，纱世里？"
    s "我在你后面！"
    mc "什……"
    "我看了一眼后面，什么都没有。"
    mc "你骗我！"
    s "嘻嘻，我说不吓你，但没说不骗你。"
    mc "麻了，你到哪了？"
    s "快了。"
    s "看你前面！"
    mc "我前面有什么好看的，没看见你。"
    s "那后面呢？"
    mc "我说过了后面没有人……"
    show sayori 1a zorder 2 at t11
    mc "哇呀，你什么时候过来的。"
    s "就刚才。"
    mc "还好，没吓到我，算你识相。"
    s "欸嘿~"
    s 3a "快走吧。"
    scene bg club_day
    $ n_name = 'TmF0c3VraQ=='
    $ y_name = 'WXVyaQ=='
    $ m_name = 'TW9uaWth'
    with dissolve_scene_full
    show sayori 4a zorder 2 at t11
    s "嗨各位~"
    show sayori 4a at t22
    show monika 5a zorder 2 at t21
    m "嗨纱世里~"
    show sayori 1a at t31
    show monika at t32
    show yuri 1a zorder 2 at t33
    y "你终于回来了。"
    show sayori at f31
    s "嘻嘻，有点事耽误了。"
    s "啊对了，我今天带了一位新成员。"
    show sayori at t41
    show monika at t42
    show yuri at t43
    show natsuki 2c zorder 2 at f44
    n "新成员？你说的就是那个男生吗？"
    show natsuki at t44
    "粉头发的女生远远地指着我。"
    show sayori 3b at f41
    s "啊是的，他就是昨天我拉的那个人。"
    show sayori at t41
    show monika 2a at f42
    m "我想起来了，我们昨天还给你出题来着。"
    show yuri 1c at f43
    y "嗯是的。"
    mc "啊…是哈…"
    show yuri at t43
    show monika at t42
    show sayori 1c at f41
    s "[player]，过来一下。"
    mc "别那样使唤我。"
    "不过我还是走了过去。"
    hide yuri
    show sayori at t31
    show monika at t32
    show natsuki at t33
    show sayori 1a
    s "我得给你介绍一下…"
    show sayori 3a
    s "这是莫妮卡，她是我们群的群主。"
    $ m_name = 'Monika'
    show monika 5a at f32
    show sayori at t31
    m "嗨！如果你有任何关于作文上的问题，欢迎随时来问我。"
    mc "唔，谢谢。"
    show monika 1a at t32
    m "我还得去问优里个问题…"
    hide monika
    show sayori at f21
    show natsuki at f22
    s "这个是夏树！"
    $ n_name = 'Natsuki'
    show natsuki 42e at f22
    n "唔…我们可不是很需要你这样的人。"
    "这娘们嘴巴好恶毒（"
    show natsuki 4u at t22
    show sayori 4r at f21
    s "嘿嘿，别在意。"
    mc "不在意不在意（）"
    show sayori 1a at t11
    hide natsuki
    s "那就好。"
    s "那么，接下来是优里…"
    show sayori 1b
    s "优里呢？"
    show sayori 4x at h11
    s "优里，你快来啊~"
    show yuri 4b at t22
    show sayori at t21
    y "啊…好的…"
    show sayori at h21
    s "快来啊~"
    show yuri 4a
    y "不要。"
    show sayori at h21
    s "快来啊——"
    show yuri at f22
    y "不要——"
    show sayori at h21
    s "让我康康！"
    show yuri at h22
    y "纱哥不要！"
    mc "欸？等会？"
    show sayori 1a
    s "啊哈哈，没事，这是个玩笑。"
    y 4b "嗯…"
    s "那么，这位是…"
    mc "优里。"
    s "哈，太对辣。"
    y "没错…"
    s "优里，介绍一下你自己。"
    y "我是三年六班…"
    mc "？"
    y "啊不是（）"
    y "我是优里。"
    mc "我知道。"
    y "啊…啊…"
    s "[player]，你别总是为难人家好吗？"
    mc "？"
    mc "行行行，宁所言极是。"
    y "我肚子不太舒服…"
    mc "所以你要走了吗？"
    y "不…"
    y "你有钱吗？我想买点药。"
    "这是社交恐惧症还是社交牛逼症啊。"
    mc "有是有…"
    "我从兜里掏出皱巴巴的十块大洋。"
    y "太好了!"
    "纱世里一把把我的十块大洋抢走了，然后递到了优里的手里。"
    y "欸？这是？"
    "优里指着我的兜，我这才发现我刚不小心把爷的方舟周边也掏出来了。"
    y "为斯卡蒂献上心脏！"
    mc "我们联合！"
    y "嘎嘎嘎嘎"
    s "这不挺投合的嘛。"
    s "我倒有点事，走了先。"
    mc "别啊。"
    "人生地不熟的，纱世里肯情就这样把我丢下来。"
    s "明儿我再来。"
    mc "？"
    s "今儿她来了，明儿我再来，这样每天都有人来，不至于太冷清，也不至于太热闹了。"
    mc "可是…"
    s "没有什么可是的。"
    mc "可是优里她也走了。"
    s "啊这"