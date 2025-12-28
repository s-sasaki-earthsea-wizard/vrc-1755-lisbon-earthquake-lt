"""
「なぜ」vs「どのように」（Why vs How）のManimアニメーション

科学的探究の本質を視覚的に表現する：
- 神学的解釈:「なぜ神はこれを起こしたのか」
- 科学的アプローチ:「どのように起きたのか」
"""

from manim import *


class WhyVsHow(Scene):
    """「なぜ」vs「どのように」をアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("科学的探究の本質", font_size=56, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 問いの転換を表示
        old_question = Text(
            "「なぜ神様はこんな災害を起こしたのか？」",
            font_size=32,
            color=RED,
        )
        old_question.move_to(UP * 1)

        self.play(FadeIn(old_question, shift=RIGHT))
        self.wait(0.5)

        # 十字架アイコン（神学的）
        cross_icon = Text("✝️", font_size=48)
        cross_icon.next_to(old_question, LEFT, buff=0.3)
        self.play(FadeIn(cross_icon), run_time=0.5)

        # 矢印で転換
        arrow = Arrow(
            start=UP * 0.3,
            end=DOWN * 0.3,
            color=YELLOW,
            buff=0.1,
        )
        arrow.move_to(ORIGIN)
        self.play(GrowArrow(arrow))

        # 新しい問い
        new_question = Text(
            "「どのように地震が起きたのか？」\n「どのような被害が起こったのか？」",
            font_size=32,
            color=BLUE,
        )
        new_question.set_line_spacing(1.3)
        new_question.move_to(DOWN * 1.2)

        # グラフアイコン（科学的）
        chart_icon = Text("📊", font_size=48)
        chart_icon.next_to(new_question, LEFT, buff=0.3)

        self.play(FadeIn(new_question, shift=RIGHT), FadeIn(chart_icon))
        self.wait(1.5)

        # フェードアウト
        self.play(
            FadeOut(old_question),
            FadeOut(cross_icon),
            FadeOut(arrow),
            FadeOut(new_question),
            FadeOut(chart_icon),
        )

        # 対比構造
        comparison_title = Text("この違いが科学的探究の本質", font_size=36, color=YELLOW)
        comparison_title.move_to(UP * 2)
        self.play(FadeIn(comparison_title, shift=UP))

        # 左側: 神学的解釈
        left_header = Text("神学的解釈", font_size=36, color=RED)
        left_header.move_to(LEFT * 3 + UP * 0.8)

        left_question = Text("「なぜ」", font_size=64, color=RED_B)
        left_question.move_to(LEFT * 3)

        left_detail = Text("神はこれを起こしたのか", font_size=24, color=GRAY_A)
        left_detail.next_to(left_question, DOWN, buff=0.3)

        # 右側: 科学的アプローチ
        right_header = Text("科学的アプローチ", font_size=36, color=BLUE)
        right_header.move_to(RIGHT * 3 + UP * 0.8)

        right_question = Text("「どのように」", font_size=56, color=BLUE_B)
        right_question.move_to(RIGHT * 3)

        right_detail = Text("起きたのか", font_size=24, color=GRAY_A)
        right_detail.next_to(right_question, DOWN, buff=0.3)

        # 中央の分割線
        divider = Line(
            start=UP * 1.2,
            end=DOWN * 1.5,
            color=GRAY,
            stroke_width=2,
        )

        # VS
        vs_text = Text("vs", font_size=40, color=YELLOW)
        vs_text.move_to(UP * 0.3)

        # 表示
        self.play(Create(divider), Write(vs_text))
        self.play(
            FadeIn(left_header, shift=RIGHT),
            FadeIn(right_header, shift=LEFT),
        )
        self.play(
            Write(left_question),
            Write(right_question),
        )
        self.play(
            FadeIn(left_detail),
            FadeIn(right_detail),
        )

        # 科学的アプローチを強調
        self.wait(1)
        box = SurroundingRectangle(
            VGroup(right_header, right_question, right_detail),
            color=GREEN,
            buff=0.3,
        )
        self.play(Create(box))

        self.wait(2)


class WhyVsHowSimple(Scene):
    """シンプル版"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("科学的探究の本質", font_size=48, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 「なぜ」
        why_label = Text("神学的解釈:", font_size=28, color=GRAY_A)
        why_text = Text("「なぜ」神はこれを起こしたのか", font_size=36, color=RED)
        why_group = VGroup(why_label, why_text).arrange(RIGHT, buff=0.3)
        why_group.move_to(UP * 1)

        self.play(FadeIn(why_group, shift=RIGHT))
        self.wait(0.5)

        # 「どのように」
        how_label = Text("科学的アプローチ:", font_size=28, color=GRAY_A)
        how_text = Text("「どのように」起きたのか", font_size=36, color=BLUE)
        how_group = VGroup(how_label, how_text).arrange(RIGHT, buff=0.3)
        how_group.move_to(DOWN * 0.5)

        self.play(FadeIn(how_group, shift=RIGHT))
        self.wait(1)

        # 強調
        self.play(
            how_text.animate.set_color(GREEN),
            run_time=0.5,
        )
        self.play(
            how_text.animate.set_color(BLUE),
            run_time=0.5,
        )

        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql why_vs_how_animation.py WhyVsHow")
    print("  manim -pql why_vs_how_animation.py WhyVsHowSimple")
