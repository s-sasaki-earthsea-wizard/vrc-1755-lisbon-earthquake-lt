"""
なぜこの地震が科学史を変えたのか（Why This Earthquake Changed Science）のManimアニメーション

1755年リスボン大地震が科学史に与えた影響を視覚的に表現する：
- 万聖節(カトリックの祝日)の朝 — 敬虔な市民が教会でミサ中に被災
- 教会が倒壊し、娼館が無傷だった矛盾
- 「なぜ神は善良な市民の街を破壊したのか？」
- 神罰説 vs 自然現象としての科学的探求 の対立
- 地震という自然災害を科学的に捉える歴史的変遷
"""

from manim import *


class WhyChangedScience(Scene):
    """科学史を変えた理由を順番にアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル表示
        title = Text("なぜこの地震が科学史を変えたのか？", font_size=56, color=WHITE)
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # セクション1: 宗教的背景
        section1_title = Text("宗教的背景", font_size=40, color=YELLOW)
        section1_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section1_title, shift=UP))

        # 項目1: 万聖節
        item1_icon = Text("🕯️", font_size=48)
        item1_text = Text("万聖節(カトリックの祝日)の朝", font_size=32, color=WHITE)
        item1_detail = Text("敬虔な市民が教会でミサ中に被災", font_size=28, color=GRAY_A)
        item1 = VGroup(item1_icon, item1_text).arrange(RIGHT, buff=0.3)
        item1_detail.next_to(item1, DOWN, buff=0.2)
        item1_group = VGroup(item1, item1_detail)
        item1_group.move_to(DOWN * 0.3)

        self.play(FadeIn(item1_group, shift=RIGHT), run_time=0.8)
        self.wait(1)
        self.play(item1_group.animate.scale(0.8).shift(UP * 1.5 + LEFT * 2))

        # 項目2: 矛盾
        item2_icon = Text("⛪", font_size=48)
        item2_text = Text("教会が倒壊し、娼館が無傷だった矛盾", font_size=32, color=WHITE)
        item2 = VGroup(item2_icon, item2_text).arrange(RIGHT, buff=0.3)
        item2.move_to(DOWN * 0.3)

        self.play(FadeIn(item2, shift=RIGHT), run_time=0.8)
        self.wait(1)
        self.play(item2.animate.scale(0.8).shift(UP * 0.5 + LEFT * 2))

        # 項目3: 問い
        item3_icon = Text("❓", font_size=48)
        item3_text = Text("「なぜ神は善良な市民の街を破壊したのか？」", font_size=30, color=ORANGE)
        item3 = VGroup(item3_icon, item3_text).arrange(RIGHT, buff=0.3)
        item3.move_to(DOWN * 0.5)

        self.play(FadeIn(item3, shift=UP), run_time=0.8)
        # 問いを強調
        self.play(item3.animate.scale(1.1), run_time=0.3)
        self.play(item3.animate.scale(1 / 1.1), run_time=0.3)
        self.wait(1)

        # フェードアウト
        self.play(
            FadeOut(section1_title),
            FadeOut(item1_group),
            FadeOut(item2),
            FadeOut(item3),
        )

        # セクション2: 思想の対立
        section2_title = Text("思想の対立", font_size=40, color=YELLOW)
        section2_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section2_title, shift=UP))

        # 神罰説 vs 科学的探求
        vs_left = Text("神罰説", font_size=48, color=RED)
        vs_center = Text("vs", font_size=36, color=WHITE)
        vs_right = Text("自然現象としての\n科学的探求", font_size=40, color=BLUE)
        vs_right.set_line_spacing(1.2)

        vs_group = VGroup(vs_left, vs_center, vs_right).arrange(RIGHT, buff=0.8)
        vs_group.move_to(ORIGIN)

        self.play(FadeIn(vs_left, shift=LEFT))
        self.play(Write(vs_center))
        self.play(FadeIn(vs_right, shift=RIGHT))

        # 対立を強調するアニメーション
        self.play(
            vs_left.animate.set_color(RED_A),
            vs_right.animate.set_color(BLUE_A),
            run_time=0.5,
        )
        self.play(
            vs_left.animate.set_color(RED),
            vs_right.animate.set_color(BLUE),
            run_time=0.5,
        )

        self.wait(1)
        self.play(vs_group.animate.shift(UP * 1))

        # 歴史的変遷
        transition_text = Text(
            "地震という自然災害を科学的に捉える歴史的変遷",
            font_size=32,
            color=GREEN,
        )
        transition_text.move_to(DOWN * 1)

        # 矢印で変遷を示す
        arrow = Arrow(
            start=LEFT * 3 + DOWN * 0.3,
            end=RIGHT * 3 + DOWN * 0.3,
            color=GREEN,
            buff=0,
        )
        arrow.next_to(transition_text, DOWN, buff=0.3)

        label_left = Text("神罰", font_size=24, color=RED_B)
        label_left.next_to(arrow, LEFT, buff=0.1)
        label_right = Text("科学", font_size=24, color=BLUE_B)
        label_right.next_to(arrow, RIGHT, buff=0.1)

        self.play(FadeIn(transition_text, shift=UP))
        self.play(GrowArrow(arrow), run_time=1)
        self.play(FadeIn(label_left), FadeIn(label_right))

        self.wait(2)

        # 最終まとめ
        self.play(
            FadeOut(section2_title),
            FadeOut(vs_group),
            FadeOut(transition_text),
            FadeOut(arrow),
            FadeOut(label_left),
            FadeOut(label_right),
        )

        summary = VGroup(
            Text("• 万聖節の朝、敬虔な市民が教会で被災", font_size=28),
            Text("• 教会が倒壊し、娼館が無傷だった矛盾", font_size=28),
            Text("• 「なぜ神は善良な市民の街を破壊したのか？」", font_size=28),
            Text("• 神罰説 vs 科学的探求の対立", font_size=28, color=ORANGE),
            Text("• 自然災害を科学的に捉える歴史的変遷", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.move_to(ORIGIN)

        for item in summary:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(2)


class WhyChangedScienceSimple(Scene):
    """シンプル版：テキストのみのアニメーション"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("なぜこの地震が科学史を変えたのか？", font_size=48, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.scale(0.7).to_edge(UP))

        # 箇条書き項目（最初のボックス）
        box1_items = [
            ("🕯️", "万聖節の朝 — 敬虔な市民が教会でミサ中に被災"),
            ("⛪", "教会が倒壊し、娼館が無傷だった矛盾"),
            ("❓", "「なぜ神は善良な市民の街を破壊したのか？」"),
        ]

        box1_group = VGroup()
        for icon, text in box1_items:
            icon_text = Text(icon, font_size=36)
            content_text = Text(text, font_size=28, color=WHITE)
            item = VGroup(icon_text, content_text).arrange(RIGHT, buff=0.3)
            box1_group.add(item)

        box1_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        box1_group.move_to(UP * 0.5)

        for item in box1_group:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.2)

        self.wait(1)
        self.play(FadeOut(box1_group))

        # 箇条書き項目（2番目のボックス）
        box2_items = [
            ("神罰説 vs 自然現象としての科学的探求", ORANGE),
            ("地震という自然災害を科学的に捉える歴史的変遷", GREEN),
        ]

        box2_group = VGroup()
        for text, color in box2_items:
            content_text = Text(f"• {text}", font_size=32, color=color)
            box2_group.add(content_text)

        box2_group.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        box2_group.move_to(ORIGIN)

        for item in box2_group:
            self.play(FadeIn(item, shift=UP * 0.3), run_time=0.8)
            self.wait(0.5)

        self.wait(2)


if __name__ == "__main__":
    # コマンドラインから実行する場合:
    # manim -pql why_changed_science_animation.py WhyChangedScience
    # manim -pql why_changed_science_animation.py WhyChangedScienceSimple
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql why_changed_science_animation.py WhyChangedScience")
    print("  manim -pql why_changed_science_animation.py WhyChangedScienceSimple")
