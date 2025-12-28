"""
リスボン大震災以前のまとめ（Pre-Disaster Summary）のManimアニメーション

リスボン大震災以前の準備期間をまとめ、次章への導入を視覚的に表現する：
- 観察記録の蓄積
- 「地震は移動する現象」という経験則
- 災害後の科学的調査を可能にする土台
"""

from manim import *


class PreDisasterSummary(Scene):
    """リスボン大震災以前のまとめをアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("ここまでのまとめ", font_size=56, color=YELLOW)
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # サブタイトル
        subtitle = Text("リスボン大震災以前の準備期間", font_size=32, color=GRAY_A)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP))

        # まとめ項目1: 観察記録の蓄積
        item1_icon = Text("📖", font_size=48)
        item1_text = Text("観察記録の蓄積", font_size=36, color=WHITE)
        item1 = VGroup(item1_icon, item1_text).arrange(RIGHT, buff=0.3)
        item1.move_to(UP * 0.5)

        self.play(FadeIn(item1, shift=RIGHT), run_time=0.8)
        self.wait(0.5)

        # まとめ項目2: 経験則
        item2_icon = Text("🌊", font_size=48)
        item2_text = Text("「地震は移動する現象」という経験則", font_size=32, color=WHITE)
        item2 = VGroup(item2_icon, item2_text).arrange(RIGHT, buff=0.3)
        item2.move_to(DOWN * 0.5)

        self.play(FadeIn(item2, shift=RIGHT), run_time=0.8)
        self.wait(1)

        # 矢印で結論へ
        arrow = Arrow(
            start=DOWN * 1.3,
            end=DOWN * 2,
            color=GREEN,
            buff=0,
        )
        self.play(GrowArrow(arrow), run_time=0.5)

        # 結論
        conclusion = Text(
            "災害後の科学的調査を可能にする土台",
            font_size=36,
            color=GREEN,
        )
        conclusion.move_to(DOWN * 2.5)

        self.play(FadeIn(conclusion, shift=UP))

        # 強調
        box = SurroundingRectangle(conclusion, color=GREEN, buff=0.2)
        self.play(Create(box))
        self.wait(1.5)

        # フェードアウト
        self.play(
            FadeOut(subtitle),
            FadeOut(item1),
            FadeOut(item2),
            FadeOut(arrow),
            FadeOut(conclusion),
            FadeOut(box),
        )

        # 次章への導入
        next_title = Text("では次に...", font_size=48, color=WHITE)
        next_title.move_to(UP * 0.5)
        self.play(FadeIn(next_title))
        self.wait(0.5)

        question = Text(
            "実際に大震災が起きたとき、\n人々はどう反応したのか？",
            font_size=40,
            color=ORANGE,
        )
        question.set_line_spacing(1.3)
        question.move_to(DOWN * 0.8)

        self.play(Write(question), run_time=1.5)

        # 問いを強調
        self.play(question.animate.scale(1.05), run_time=0.3)
        self.play(question.animate.scale(1 / 1.05), run_time=0.3)

        self.wait(2)


class PreDisasterSummarySimple(Scene):
    """シンプル版"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # まとめタイトル
        title = Text("ここまでのまとめ", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # まとめ項目
        items = VGroup(
            Text("📖 観察記録の蓄積", font_size=36),
            Text("🌊 「地震は移動する現象」という経験則", font_size=32),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        items.move_to(UP * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.3)

        # 結論
        conclusion = Text(
            "→ 災害後の科学的調査を可能にする土台",
            font_size=32,
            color=GREEN,
        )
        conclusion.move_to(DOWN * 1)
        self.play(FadeIn(conclusion, shift=UP))
        self.wait(1.5)

        # フェードアウトして次章へ
        self.play(FadeOut(items), FadeOut(conclusion))

        # 次章導入
        next_text = Text(
            "では次に、実際に大震災が起きたとき\n人々はどう反応したのか見ていきましょう",
            font_size=32,
            color=WHITE,
        )
        next_text.set_line_spacing(1.3)
        self.play(FadeIn(next_text))
        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql pre_disaster_summary_animation.py PreDisasterSummary")
    print("  manim -pql pre_disaster_summary_animation.py PreDisasterSummarySimple")
