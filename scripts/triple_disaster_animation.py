"""
三重の災害（Triple Disaster）のManimアニメーション

1755年リスボン大地震における3つの災害を視覚的に表現する：
1. 地震: 建物の倒壊（3回の大きな揺れ）
2. 津波: 海水が一度引いた後、巨大な波が襲来
3. 火災: 調理器具の転倒などにより市内各所で発生
"""

from manim import *


class TripleDisaster(Scene):
    """三重の災害を順番にアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定（環境に応じて調整が必要な場合あり）
        Text.set_default(font="Hiragino Sans")

        # タイトル表示
        title = Text("三重の災害", font_size=72, color=WHITE)
        subtitle = Text("1755年リスボン大地震", font_size=36, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # 災害リストの作成
        disasters = [
            {
                "number": "1",
                "title": "地震",
                "description": "建物の倒壊（3回の大きな揺れ）",
                "color": ORANGE,
                "icon": self.create_earthquake_icon(),
            },
            {
                "number": "2",
                "title": "津波",
                "description": "海水が一度引いた後、巨大な波が襲来",
                "color": BLUE,
                "icon": self.create_tsunami_icon(),
            },
            {
                "number": "3",
                "title": "火災",
                "description": "調理器具の転倒などにより市内各所で発生",
                "color": RED,
                "icon": self.create_fire_icon(),
            },
        ]

        # 各災害を順番に表示
        displayed_items = VGroup()

        for i, disaster in enumerate(disasters):
            item = self.create_disaster_item(disaster, i)
            displayed_items.add(item)

            # アニメーション効果
            self.play(
                FadeIn(item, shift=RIGHT),
                run_time=0.8,
            )

            # アイコンの強調アニメーション
            icon = item[0]  # アイコン部分
            self.play(
                icon.animate.scale(1.2),
                run_time=0.3,
            )
            self.play(
                icon.animate.scale(1 / 1.2),
                run_time=0.3,
            )

            self.wait(0.5)

        # 全体を少し待機
        self.wait(1)

        # 全体を強調表示
        self.play(
            displayed_items.animate.set_color(WHITE),
            run_time=0.5,
        )
        self.play(
            displayed_items.animate.set_color(YELLOW),
            run_time=0.5,
        )
        self.play(
            displayed_items.animate.set_color(WHITE),
            run_time=0.5,
        )

        self.wait(2)

    def create_disaster_item(self, disaster: dict, index: int) -> VGroup:
        """災害項目のビジュアル要素を作成"""
        # 番号バッジ
        badge = Circle(radius=0.3, color=disaster["color"], fill_opacity=0.8)
        number = Text(disaster["number"], font_size=24, color=WHITE)
        number.move_to(badge.get_center())
        badge_group = VGroup(badge, number)

        # タイトル（太字）
        title = Text(disaster["title"], font_size=48, color=disaster["color"])
        title.next_to(badge_group, RIGHT, buff=0.3)

        # 説明文
        description = Text(disaster["description"], font_size=28, color=GRAY_A)
        description.next_to(title, RIGHT, buff=0.3)

        # アイコン
        icon = disaster["icon"]
        icon.scale(0.5)
        icon.next_to(description, RIGHT, buff=0.5)

        # グループ化
        item = VGroup(icon, badge_group, title, description)
        item.move_to(ORIGIN)
        item.shift(UP * (1.5 - index * 1.5))  # 縦に配置

        return item

    def create_earthquake_icon(self) -> VGroup:
        """地震アイコン（揺れる建物）を作成"""
        # 建物
        building = Rectangle(width=0.8, height=1.2, color=ORANGE, fill_opacity=0.7)
        # 揺れ線
        lines = VGroup()
        for i in range(3):
            line = Line(
                start=LEFT * 0.6 + UP * (0.3 * i - 0.3),
                end=LEFT * 0.3 + UP * (0.3 * i - 0.2),
                color=ORANGE,
            )
            lines.add(line)

        return VGroup(building, lines)

    def create_tsunami_icon(self) -> VGroup:
        """津波アイコン（波）を作成"""
        # 波の曲線
        wave = FunctionGraph(
            lambda x: 0.3 * np.sin(2 * x),
            x_range=[-1, 1],
            color=BLUE,
        )
        wave2 = FunctionGraph(
            lambda x: 0.2 * np.sin(2 * x + 0.5) - 0.4,
            x_range=[-1, 1],
            color=BLUE_B,
        )

        return VGroup(wave, wave2)

    def create_fire_icon(self) -> VGroup:
        """火災アイコン（炎）を作成"""
        # 炎の形状（簡易版）
        flame = Polygon(
            [0, 0.6, 0],
            [-0.3, -0.3, 0],
            [-0.1, 0, 0],
            [0, -0.4, 0],
            [0.1, 0, 0],
            [0.3, -0.3, 0],
            color=RED,
            fill_opacity=0.8,
        )
        inner_flame = Polygon(
            [0, 0.3, 0],
            [-0.15, -0.1, 0],
            [0, -0.2, 0],
            [0.15, -0.1, 0],
            color=YELLOW,
            fill_opacity=0.9,
        )

        return VGroup(flame, inner_flame)


class TripleDisasterSimple(Scene):
    """シンプル版：テキストのみのアニメーション"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("三重の災害", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 箇条書き項目
        items = [
            ("1. 地震", "建物の倒壊（3回の大きな揺れ）", ORANGE),
            ("2. 津波", "海水が一度引いた後、巨大な波が襲来", BLUE),
            ("3. 火災", "調理器具の転倒などにより市内各所で発生", RED),
        ]

        bullet_group = VGroup()

        for i, (label, desc, color) in enumerate(items):
            # ラベル部分
            label_text = Text(label, font_size=40, color=color)
            # 説明部分
            desc_text = Text(desc, font_size=28, color=GRAY_A)
            desc_text.next_to(label_text, DOWN, aligned_edge=LEFT, buff=0.2)

            item_group = VGroup(label_text, desc_text)
            item_group.shift(DOWN * (i * 1.8) + UP * 1.5 + LEFT * 2)

            bullet_group.add(item_group)

        # 順番にフェードイン
        for item in bullet_group:
            self.play(FadeIn(item, shift=RIGHT * 0.5), run_time=0.8)
            self.wait(0.3)

        self.wait(2)

        # 最後にすべて強調
        self.play(
            *[item[0].animate.scale(1.1) for item in bullet_group],
            run_time=0.5,
        )
        self.play(
            *[item[0].animate.scale(1 / 1.1) for item in bullet_group],
            run_time=0.5,
        )

        self.wait(1)


if __name__ == "__main__":
    # コマンドラインから実行する場合:
    # manim -pql triple_disaster_animation.py TripleDisaster
    # manim -pql triple_disaster_animation.py TripleDisasterSimple
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql triple_disaster_animation.py TripleDisaster")
    print("  manim -pql triple_disaster_animation.py TripleDisasterSimple")
