from pyecharts.charts import Bar
import pandas as pd
from pyecharts import options as opts

result = pd.read_csv('bar.csv')

# 柱状图创建
bars = Bar(init_opts=opts.InitOpts(theme='dark'))

# 添加值
bars.add_xaxis(list(result['time'])),
bars.add_yaxis("纯点", list(result['纯点']), stack="stack1"),
bars.add_yaxis("混动", list(result['混动']), stack="stack1"),
bars.add_yaxis("燃油", list(result['燃油']), stack="stack1"),

# 配置
bars.set_global_opts(

    # 图表标题
    title_opts=opts.TitleOpts(
        # 标题
        title="车辆运行模式",
        # 标题位置
        pos_left="left",
        # 标题字体大小设置为 20
        title_textstyle_opts=opts.TextStyleOpts(font_size=20)
    ),

    # 图例设置
    legend_opts=opts.LegendOpts(
        # 显示图例，就是各个指标的切换按钮
        is_show=True,
        # 图例设置为单选模式(multiple 多选)
        selected_mode='multiple',
        # 图例的位置
        # pos_top='5%', pos_right='50%',
        # 图例的布局朝向，水平(vertical 垂直)
        orient='horizontal',
        # 图例形状
        legend_icon='circle'
    ),

    # 工具箱设置
    toolbox_opts=opts.ToolboxOpts(
        # 是否显示工具栏组件
        is_show=True,
        # 布局朝向('vertical')
        orient='vertical',
        # 离上边距的距离
        pos_top='10%',
        # 离左边距的距离
        pos_left='91%',

        # 配置各个工具箱
        feature=opts.ToolBoxFeatureOpts(

            # 保存工具
            opts.ToolBoxFeatureSaveAsImageOpts(
                # 是否显示
                is_show=True,
                # 提示语
                title="保存",
            ),

            # 还原工具
            opts.ToolBoxFeatureRestoreOpts(
                # 是否显示该工具
                is_show=True,
                # 提示语
                title="还原",
            ),

            # 数据视图工具
            opts.ToolBoxFeatureDataViewOpts(
                # 是否显示该工具
                is_show=True,
                # 提示语
                title="数据视图",
                # 是否不可编辑
                is_read_only=False,
            ),

            # 缩放工具配置项，直角坐标系适用
            opts.ToolBoxFeatureDataZoomOpts(
                # 是否显示该工具。
                is_show=True,
                # 提示语
                zoom_title="区域缩放",
                # 提示语
                back_title="缩放还原",
            ),

            # 图表类型切换，适用于直角坐标系
            opts.ToolBoxFeatureMagicTypeOpts(
                # 是否显示该工具
                is_show=True,
                # 启用的动态类型('stack','line','bar','tiled')
                type_=['stack', 'line', 'bar', 'tiled'],
                # 折线标题文本
                line_title="折线图",
                # 柱状标题文本
                bar_title="柱状图",
                # 堆积标题文本
                stack_title="堆叠",
                # 平铺标题文
                tiled_title="平铺",
            ),

            # 工具箱选框组件配置项
            opts.ToolBoxFeatureBrushOpts(
                # 选择显示哪些选框
                type_=[]
            ),
        )
    ),
)
bars.render('bar.html')