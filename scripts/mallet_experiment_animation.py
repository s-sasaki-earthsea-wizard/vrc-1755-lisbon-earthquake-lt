"""
マレットの爆破実験（Mallet's Explosion Experiment）のManimアニメーション

ロバート・マレットの1849年爆破実験を視覚的に表現する：
- 地下に爆薬を埋めて爆破
- 約800メートル離れた場所で地震波を測定
- 濡れた砂: 秒速約251メートル
- 花崗岩: 秒速約427メートル
- 媒質によって伝播速度が異なることを実証
"""

from manim import *


class MalletExperiment(Scene):
    """マレットの爆破実験をアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("マレットの爆破実験 (1849年)", font_size=48, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.scale(0.7).to_edge(UP))

        # 地面のライン
        ground = Line(
            start=LEFT * 6,
            end=RIGHT * 6,
            color=DARK_BROWN,
            stroke_width=4,
        )
        ground.move_to(DOWN * 1)

        # 地下部分（媒質）
        underground = Rectangle(
            width=12,
            height=2,
            color=DARK_BROWN,
            fill_opacity=0.3,
            stroke_width=0,
        )
        underground.move_to(DOWN * 2)

        self.play(Create(ground), FadeIn(underground))

        # 爆発地点
        explosion_point = Dot(point=LEFT * 4 + DOWN * 1.5, color=RED, radius=0.15)
        explosion_label = Text("💣 爆薬", font_size=24, color=RED)
        explosion_label.next_to(explosion_point, DOWN, buff=0.2)

        # 測定地点
        measure_point = Dot(point=RIGHT * 4 + DOWN * 1, color=BLUE, radius=0.15)
        measure_label = Text("📡 測定地点", font_size=24, color=BLUE)
        measure_label.next_to(measure_point, UP, buff=0.2)

        # 距離表示
        distance_line = Line(
            start=LEFT * 4 + DOWN * 0.5,
            end=RIGHT * 4 + DOWN * 0.5,
            color=YELLOW,
            stroke_width=2,
        )
        distance_label = Text("約800m", font_size=24, color=YELLOW)
        distance_label.next_to(distance_line, UP, buff=0.1)

        self.play(
            FadeIn(explosion_point),
            FadeIn(explosion_label),
            FadeIn(measure_point),
            FadeIn(measure_label),
        )
        self.play(Create(distance_line), FadeIn(distance_label))
        self.wait(0.5)

        # 爆発アニメーション
        explosion = Circle(radius=0.1, color=ORANGE, fill_opacity=0.8)
        explosion.move_to(explosion_point.get_center())

        self.play(
            explosion.animate.scale(5).set_opacity(0),
            run_time=0.5,
        )
        self.remove(explosion)

        # 地震波の伝播
        for _ in range(2):
            wave = Circle(radius=0.1, color=ORANGE, stroke_width=3)
            wave.move_to(explosion_point.get_center())
            self.play(
                wave.animate.scale(50).set_opacity(0),
                run_time=1.5,
                rate_func=linear,
            )
            self.remove(wave)

        # フェードアウト
        self.play(
            FadeOut(ground),
            FadeOut(underground),
            FadeOut(explosion_point),
            FadeOut(explosion_label),
            FadeOut(measure_point),
            FadeOut(measure_label),
            FadeOut(distance_line),
            FadeOut(distance_label),
        )

        # 測定結果
        result_title = Text("測定結果", font_size=40, color=YELLOW)
        result_title.move_to(UP * 2)
        self.play(FadeIn(result_title, shift=UP))

        # 媒質ごとの速度比較
        # 濡れた砂
        sand_label = Text("濡れた砂:", font_size=32, color=GOLD)
        sand_value = Text("秒速 約251m", font_size=40, color=GOLD)
        sand_group = VGroup(sand_label, sand_value).arrange(RIGHT, buff=0.5)
        sand_group.move_to(UP * 0.5)

        # 棒グラフ（砂）
        sand_bar = Rectangle(
            width=2.51,
            height=0.5,
            color=GOLD,
            fill_opacity=0.7,
        )
        sand_bar.move_to(UP * 0.5 + RIGHT * 1.5)

        # 花崗岩
        granite_label = Text("花崗岩:", font_size=32, color=GRAY_B)
        granite_value = Text("秒速 約427m", font_size=40, color=GRAY_B)
        granite_group = VGroup(granite_label, granite_value).arrange(RIGHT, buff=0.5)
        granite_group.move_to(DOWN * 0.8)

        # 棒グラフ（花崗岩）
        granite_bar = Rectangle(
            width=4.27,
            height=0.5,
            color=GRAY_B,
            fill_opacity=0.7,
        )
        granite_bar.move_to(DOWN * 0.8 + RIGHT * 2.4)

        # 表示（テキストのみ）
        self.play(FadeIn(sand_group, shift=RIGHT))
        self.wait(0.5)
        self.play(FadeIn(granite_group, shift=RIGHT))
        self.wait(1)

        # フェードアウトして結論へ
        self.play(
            FadeOut(sand_group),
            FadeOut(granite_group),
        )

        # 結論
        conclusion = Text(
            "媒質によって伝播速度が異なることを実証",
            font_size=36,
            color=GREEN,
        )
        conclusion.move_to(ORIGIN)

        self.play(Write(conclusion), run_time=1.5)

        # 強調ボックス
        box = SurroundingRectangle(conclusion, color=GREEN, buff=0.3)
        self.play(Create(box))

        significance = Text(
            "→ 地震波の性質を理解する重要な発見",
            font_size=28,
            color=GRAY_A,
        )
        significance.next_to(box, DOWN, buff=0.5)
        self.play(FadeIn(significance, shift=UP))

        self.wait(2)


class MalletExperimentSimple(Scene):
    """シンプル版"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("マレットの爆破実験 (1849年)", font_size=40, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 実験概要
        overview = Text(
            "地下で爆薬を爆破し、約800m離れた場所で地震波を測定",
            font_size=28,
            color=GRAY_A,
        )
        overview.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(overview, shift=UP))
        self.wait(1)

        # 測定結果
        results = VGroup(
            Text("• 濡れた砂: 秒速 約251m", font_size=32, color=GOLD),
            Text("• 花崗岩:   秒速 約427m", font_size=32, color=GRAY_B),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        results.move_to(UP * 0.2)

        for item in results:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.3)

        self.wait(1)

        # 結論
        conclusion = Text(
            "→ 媒質によって伝播速度が異なることを実証",
            font_size=32,
            color=GREEN,
        )
        conclusion.move_to(DOWN * 1.5)
        self.play(FadeIn(conclusion, shift=UP))

        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql mallet_experiment_animation.py MalletExperiment")
    print("  manim -pql mallet_experiment_animation.py MalletExperimentSimple")
