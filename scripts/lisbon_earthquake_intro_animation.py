"""
リスボン大震災概要（Lisbon Earthquake Introduction）のManimアニメーション

1755年リスボン大地震の基本情報を視覚的に表現する：
- ポルトガルの首都リスボンを襲った大地震
- 発生日時: 1755年11月1日 午前9時40分頃
- 震源: 大西洋、サン・ヴィンセント岬沖 約220km
"""

from manim import *


class LisbonEarthquakeIntro(Scene):
    """リスボン大震災の概要を順番にアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル表示
        title = Text("リスボン大震災", font_size=72, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 1. 概要説明
        intro_text = Text(
            "ポルトガルの首都リスボンを襲った大地震",
            font_size=36,
            color=WHITE,
        )
        intro_text.move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(intro_text, shift=UP), run_time=1)
        self.wait(1)

        # 地図表示用の空欄（後で編集で挿入）
        self.wait(2)

        self.play(FadeOut(intro_text))

        # 2. 発生日時
        date_label = Text("発生日時", font_size=36, color=YELLOW)
        date_value = Text("1755年11月1日", font_size=56, color=WHITE)
        time_value = Text("午前9時40分頃", font_size=48, color=ORANGE)

        date_group = VGroup(date_label, date_value, time_value).arrange(DOWN, buff=0.4)
        date_group.move_to(ORIGIN)

        self.play(FadeIn(date_label, shift=UP))
        self.play(Write(date_value), run_time=1)

        # 時計アイコン
        clock = self.create_clock_icon()
        clock.scale(0.6)
        clock.next_to(time_value, LEFT, buff=0.5)

        self.play(
            Write(time_value),
            FadeIn(clock),
            run_time=1,
        )

        # 時計の針を動かすアニメーション
        self.wait(1.5)
        self.play(FadeOut(date_group), FadeOut(clock))

        # 3. 震源
        epicenter_label = Text("震源", font_size=36, color=YELLOW)
        epicenter_location = Text("大西洋", font_size=48, color=BLUE)
        epicenter_detail = Text(
            "サン・ヴィンセント岬沖 約220km",
            font_size=36,
            color=GRAY_A,
        )

        epicenter_group = VGroup(
            epicenter_label, epicenter_location, epicenter_detail
        ).arrange(DOWN, buff=0.4)
        epicenter_group.move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(epicenter_label, shift=UP))
        self.play(Write(epicenter_location), run_time=0.8)
        self.play(FadeIn(epicenter_detail, shift=UP), run_time=0.8)

        # 震源を示す波紋アニメーション
        epicenter_dot = Dot(color=RED, radius=0.15)
        epicenter_dot.move_to(DOWN * 1.5)

        self.play(FadeIn(epicenter_dot, scale=0.5))

        # 波紋エフェクト
        for _ in range(3):
            wave = Circle(radius=0.1, color=RED, stroke_width=3)
            wave.move_to(epicenter_dot.get_center())
            self.play(
                wave.animate.scale(10).set_opacity(0),
                run_time=1,
            )
            self.remove(wave)

        self.wait(0.5)
        self.play(
            FadeOut(epicenter_group),
            FadeOut(epicenter_dot),
        )

        # 最終まとめ
        summary = VGroup(
            Text("• ポルトガルの首都リスボンを襲った大地震", font_size=32),
            Text("• 発生日時: 1755年11月1日 午前9時40分頃", font_size=32),
            Text("• 震源: 大西洋、サン・ヴィンセント岬沖 約220km", font_size=32),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary.move_to(ORIGIN)

        for item in summary:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)

        self.wait(2)

    def create_clock_icon(self) -> VGroup:
        """時計アイコンを作成"""
        clock_face = Circle(radius=0.5, color=WHITE, stroke_width=2)

        # 時針（9時40分を指す）
        hour_hand = Line(ORIGIN, UP * 0.25 + LEFT * 0.1, color=WHITE, stroke_width=3)
        minute_hand = Line(ORIGIN, UP * 0.4, color=WHITE, stroke_width=2)

        # 中心点
        center_dot = Dot(ORIGIN, color=WHITE, radius=0.05)

        return VGroup(clock_face, hour_hand, minute_hand, center_dot)


class LisbonEarthquakeIntroSimple(Scene):
    """シンプル版：テキストのみのアニメーション"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("リスボン大震災", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 箇条書き項目
        items = [
            ("概要", "ポルトガルの首都リスボンを襲った大地震", WHITE),
            ("発生日時", "1755年11月1日 午前9時40分頃", ORANGE),
            ("震源", "大西洋、サン・ヴィンセント岬沖 約220km", BLUE),
        ]

        bullet_group = VGroup()

        for i, (label, value, color) in enumerate(items):
            # ラベル部分
            label_text = Text(f"• {label}:", font_size=32, color=YELLOW)
            # 値部分
            value_text = Text(value, font_size=32, color=color)
            value_text.next_to(label_text, DOWN, aligned_edge=LEFT, buff=0.15)

            item_group = VGroup(label_text, value_text)
            item_group.shift(DOWN * (i * 1.8) + UP * 1 + LEFT * 2)

            bullet_group.add(item_group)

        # 順番にフェードイン
        for item in bullet_group:
            self.play(
                FadeIn(item[0], shift=RIGHT * 0.3),
                run_time=0.5,
            )
            self.play(
                FadeIn(item[1], shift=UP * 0.2),
                run_time=0.6,
            )
            self.wait(0.3)

        self.wait(2)


if __name__ == "__main__":
    # コマンドラインから実行する場合:
    # manim -pql lisbon_earthquake_intro_animation.py LisbonEarthquakeIntro
    # manim -pql lisbon_earthquake_intro_animation.py LisbonEarthquakeIntroSimple
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql lisbon_earthquake_intro_animation.py LisbonEarthquakeIntro")
    print("  manim -pql lisbon_earthquake_intro_animation.py LisbonEarthquakeIntroSimple")
