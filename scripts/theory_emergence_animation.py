"""
理論の萌芽（Emergence of Theory）のManimアニメーション

1750年ロンドン地震の観察から生まれた科学的概念を視覚的に表現する：
- 地震の「軌道」概念
- 場所によって揺れの到達時刻・強度が異なる
- 地震は「移動する現象」
- 現代の「震源からの地震波伝播」の経験則
"""

from manim import *


class TheoryEmergence(Scene):
    """理論の萌芽をアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル表示
        title = Text("理論の萌芽", font_size=72, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # サブタイトル
        subtitle = Text("1750年ロンドン地震の観察", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP))

        # 地震の「軌道」概念を視覚化
        concept_text = Text("地震の「軌道」概念", font_size=40, color=ORANGE)
        concept_text.move_to(UP * 1)
        self.play(Write(concept_text), run_time=1)
        self.wait(0.5)
        self.play(concept_text.animate.scale(0.7).shift(UP * 0.5))

        # 震源から波が広がるアニメーション
        epicenter = Dot(point=LEFT * 3, color=RED, radius=0.15)
        epicenter_label = Text("震源", font_size=20, color=RED)
        epicenter_label.next_to(epicenter, DOWN, buff=0.2)

        # 観測点を配置
        observers = VGroup()
        observer_positions = [LEFT * 1, ORIGIN, RIGHT * 1.5, RIGHT * 3]
        observer_labels = ["A地点", "B地点", "C地点", "D地点"]

        for pos, label in zip(observer_positions, observer_labels):
            dot = Dot(point=pos + DOWN * 0.5, color=BLUE, radius=0.1)
            text = Text(label, font_size=16, color=BLUE_B)
            text.next_to(dot, DOWN, buff=0.1)
            observers.add(VGroup(dot, text))

        self.play(
            FadeIn(epicenter),
            FadeIn(epicenter_label),
        )
        self.play(FadeIn(observers))

        # 波の伝播アニメーション（D地点まで到達する大きさ）
        for i in range(3):
            wave = Circle(radius=0.1, color=ORANGE, stroke_width=2)
            wave.move_to(epicenter.get_center())
            self.play(
                wave.animate.scale(65).set_opacity(0),
                run_time=1.5,
                rate_func=linear,
            )
            self.remove(wave)

        # 説明テキスト
        explanation1 = Text(
            "場所によって揺れの到達時刻・強度が異なる",
            font_size=28,
            color=WHITE,
        )
        explanation1.move_to(DOWN * 2.8)
        self.play(FadeIn(explanation1, shift=UP))
        self.wait(1)

        # 矢印で「移動する現象」を示す
        arrow = Arrow(
            start=LEFT * 3 + DOWN * 1.5,
            end=RIGHT * 3 + DOWN * 1.5,
            color=GREEN,
            buff=0,
        )
        arrow_label = Text("地震は「移動する現象」", font_size=24, color=GREEN)
        arrow_label.next_to(arrow, DOWN, buff=0.2)

        self.play(GrowArrow(arrow), run_time=1)
        self.play(FadeIn(arrow_label))
        self.wait(1)

        # フェードアウト
        self.play(
            FadeOut(concept_text),
            FadeOut(epicenter),
            FadeOut(epicenter_label),
            FadeOut(observers),
            FadeOut(explanation1),
            FadeOut(arrow),
            FadeOut(arrow_label),
        )

        # 現代との接続
        modern_text = Text(
            "現代の「震源からの地震波伝播」が経験則として認識",
            font_size=30,
            color=WHITE,
        )
        modern_text.move_to(ORIGIN)
        self.play(FadeIn(modern_text, shift=UP))
        self.wait(1)
        self.play(FadeOut(modern_text))

        # 結論
        conclusion_icon = Text("💡", font_size=64)
        conclusion_text = Text(
            "地震を科学的に解釈しようとする萌芽",
            font_size=40,
            color=YELLOW,
        )
        conclusion = VGroup(conclusion_icon, conclusion_text).arrange(RIGHT, buff=0.3)
        conclusion.move_to(ORIGIN)

        self.play(FadeIn(conclusion, scale=0.8))

        # 強調
        self.play(conclusion.animate.scale(1.1), run_time=0.3)
        self.play(conclusion.animate.scale(1 / 1.1), run_time=0.3)

        self.wait(2)


class TheoryEmergenceSimple(Scene):
    """シンプル版：テキストのみのアニメーション"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("理論の萌芽", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 1750年ロンドン地震
        header = Text("1750年ロンドン地震の観察", font_size=36, color=YELLOW)
        header.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(header, shift=UP))

        # 箇条書き
        items = VGroup(
            Text("• 地震の「軌道」概念", font_size=32, color=ORANGE),
            Text("• 場所によって揺れの到達時刻・強度が異なる", font_size=28, color=WHITE),
            Text("  → 地震は「移動する現象」", font_size=28, color=GREEN),
            Text("• 現代の「震源からの地震波伝播」の経験則", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(DOWN * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.2)

        self.wait(1)
        self.play(FadeOut(items), FadeOut(header))

        # 結論
        conclusion = VGroup(
            Text("💡", font_size=56),
            Text("地震を科学的に解釈しようとする萌芽", font_size=36, color=YELLOW),
        ).arrange(RIGHT, buff=0.3)
        conclusion.move_to(ORIGIN)

        self.play(FadeIn(conclusion, scale=0.9))
        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql theory_emergence_animation.py TheoryEmergence")
    print("  manim -pql theory_emergence_animation.py TheoryEmergenceSimple")
