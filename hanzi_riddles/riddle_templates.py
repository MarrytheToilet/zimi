riddle_templates = {
    "train": {
        'B': [
            "上面是{0}，下面是{1}",
            "上半部{0}，下半部{1}",
            "上边承载{0}，下边承载{1}",
            "顶部展示{0}，底部展示{1}",
            "上{0}下{1}，合为一体",
            "上方{0}如峰巅之望，下处{1}似谷底之思",
            "画中{0}盛开云端，画中{1}默落画底",
            "诗的{0}首句辉映；诗的{1}尾韵沉淀",
            "云上是{0}的舞，地下是{1}的步",
            "塔顶{0}挑战苍穹，基座{1}镇守大地",
            "河的源头有{0}的波涛，彼岸有{1}的静谧",
            "天空翱翔{0}，大地奔腾{1}",
            "火上{0}炽烈如歌，灰下{1}沉静如诉"
        ],
        'H': [
            "左边是{0}，右边是{1}",
            "左侧执{0}，右侧持{1}",
            "左部分{0}，右部分{1}",
            "左{0}右{1}，互为表里",
            "左侧{0}，右侧{1}，共同构成全貌",
            "弓的左侧，{0}待发之势；弓的右侧，{1}射出之力",
            "门的左扇，{0}装饰之美；门的右扇，{1}简约之雅",
            "左手创{0}，右手绘{1}",
            "左翼{0}展飞之姿；右翼{1}平稳之态",
            "左岸{0}繁华，右岸{1}静谧",
            "梦想左眼{0}，现实右眼{1}"
        ],
        'E': [
            "上面是{0}，中间是{1}，下面是{2}",
            "顶上{0}，中段{1}，底下{2}",
            "上层{0}高悬，中部{1}稳固，下方{2}扎实",
            "上{0}如天，中{1}如人，下{2}如地",
            "上端{0}遥望，中间{1}平稳，底部{2}沉稳",
            "上{0}如同天空的日出，中{1}如同午间的烈阳，下{2}如同黄昏的晚霞",
            "上{0}开花，中{1}结实，下{2}扎根",
            "上层{0}飘逸，中层{1}凝练，下层{2}沉着",
            "上段{0}轻盈如风，中段{1}稳如山，下段{2}厚重如地",
            "上头{0}点缀，中间{1}连接，下端{2}支撑"
        ],
        'M': [
            "左边是{0}，中间是{1}，右边是{2}",
            "左{0}居左，中{1}居中，右{2}居右",
            "左侧{0}如云，中间{1}如山，右侧{2}如水",
            "左边{0}引导，中间{1}支撑，右边{2}结束",
            "左翼{0}展开，中翼{1}稳固，右翼{2}收拢",
            "左{0}先行，中{1}跟随，右{2}压阵",
            "左起{0}，中程{1}，右落{2}",
            "左{0}宽阔，中{1}凝聚，右{2}锐利",
            "左翼{0}飞扬，中间{1}安稳，右翼{2}内敛",
            "左手{0}开拓，中间{1}协调，右手{2}收尾"
        ],
        'Q': [
            "外圈{0}围绕，内里{1}守护",
            "外部{0}包围，内部{1}藏匿",
            "外围{0}环绕，中心{1}静谧",
            "外部{0}如城，内部{1}如府",
            "外面是{0}，里面是{1}",
            "外围{0}如盾，中心{1}如心",
            "外部{0}强大，内部{1}坚固",
            "外壳{0}保护，内核{1}精华",
            "外{0}庇护，中{1}藏匿",
            "外圈{0}牢不可破，内心{1}宁静致远"
        ]
    },
    "test": {
        'B': [
            "上方{0}，下方{1}",
            "高处{0}，低处{1}",
            "上{0}与下{1}",
            "上层{0}，下层{1}",
            "顶端{0}，基底{1}",
            "日出{0}辉映天际，夜幕{1}铺满地面",
            "树冠{0}枝繁叶茂，根系{1}深埋大地",
            "山巅{0}雪白皑皑，山脚{1}石坚如铁",
            "楼阁{0}眺望天际，底层{1}沉思地面",
            "星空{0}辽阔无垠，大地{1}宽广无际"
        ],
        'H': [
            "左面{0}，右面{1}",
            "左侧{0}，右侧{1}",
            "左{0}对右{1}",
            "左部{0}，右部{1}",
            "左边{0}，右边{1}",
            "左侧{0}浓烈，右侧{1}淡雅",
            "左岸{0}波涛汹涌，右岸{1}波澜不惊",
            "左手的{0}温柔细腻，右手的{1}力量十足",
            "左肩{0}担当重任，右肩{1}守护安宁"
        ],
        'E': [
            "顶端{0}，中段{1}，底端{2}",
            "上{0}天，中{1}地，下{2}海",
            "上部{0}光明，中部{1}坚实，下部{2}厚重",
            "高空{0}飘渺，中层{1}宁静，地面{2}厚实",
            "上头{0}灵动，中间{1}稳重，下方{2}坚韧",
            "山顶{0}俯视大地，中部{1}平和，山脚{2}扎根",
            "上段{0}映照，中段{1}沉默，下段{2}积淀",
            "上层{0}展望，中层{1}守望，下层{2}体会",
            "上方{0}如日，中间{1}如月，下方{2}如星",
            "天空{0}辽远，中间{1}厚重，大地{2}无垠"
        ],
        'M': [
            "左部{0}撑起，中部{1}连接，右部{2}收束",
            "左{0}与右{2}，中间{1}连接",
            "左边{0}，中间{1}，右边{2}",
            "左方{0}壮阔，中部{1}沉稳，右方{2}灵巧",
            "左手{0}，右手{2}，中间{1}",
            "左翼{0}策马奔腾，中翼{1}坚如磐石，右翼{2}翱翔天际",
            "左{0}力量，中{1}智慧，右{2}速度",
            "左岸{0}绿树，中流{1}黄沙，右岸{2}青山",
            "左起{0}之光，中间{1}之韵，右落{2}之影",
            "左{0}风，中{1}火，右{2}雷"
        ],
        'Q': [
            "外部{0}坚固，内部{1}柔软",
            "外圈{0}覆盖，内心{1}安然",
            "外层{0}厚重，内层{1}轻盈",
            "外{0}庇护，内{1}核心",
            "外壳{0}坚硬，内里{1}温暖",
            "外界{0}变幻无常，内心{1}坚定不移",
            "外{0}防守，内{1}珍藏",
            "外圈{0}环绕，中芯{1}坚守",
            "外壁{0}强韧，内芯{1}柔软",
            "外{0}如墙，内{1}如玉"
        ]
    }
}
