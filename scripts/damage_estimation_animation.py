"""
被害想定（Damage Estimation）のManimアニメーション

1755年リスボン大地震の被害規模を視覚的に表現する：
- 推定マグニチュード: M8.5〜9
- 死者数: 3万〜4万人
- リスボン市内の建物の約85%が破壊
"""

from manim import *


class DamageEstimation(Scene):
    """被害想定を順番にアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル表示
        title = Text("被害想定", font_size=72, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 1. マグニチュード
        mag_label = Text("推定マグニチュード", font_size=36, color=YELLOW)
        mag_value = Text("M8.5〜9", font_size=72, color=RED)
        mag_group = VGroup(mag_label, mag_value).arrange(DOWN, buff=0.3)
        mag_group.move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(mag_label, shift=UP))
        self.play(
            Write(mag_value),
            run_time=1,
        )
        # 揺れるアニメーション
        self.play(
            mag_value.animate.shift(LEFT * 0.1),
            run_time=0.1,
        )
        self.play(
            mag_value.animate.shift(RIGHT * 0.2),
            run_time=0.1,
        )
        self.play(
            mag_value.animate.shift(LEFT * 0.1),
            run_time=0.1,
        )
        self.wait(1)
        self.play(FadeOut(mag_group))

        # 2. 死者数
        death_label = Text("死者数", font_size=36, color=YELLOW)
        death_value = Text("3万〜4万人", font_size=72, color=RED)
        death_group = VGroup(death_label, death_value).arrange(DOWN, buff=0.3)
        death_group.move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(death_label, shift=UP))

        # カウントアップアニメーション
        counter = Integer(0, font_size=72, color=RED)
        counter.move_to(death_value.get_center())

        self.play(FadeIn(counter))
        self.play(
            counter.animate.set_value(30000),
            run_time=2,
            rate_func=smooth,
        )

        # 数値をテキストに置き換え
        self.play(
            FadeOut(counter),
            FadeIn(death_value),
        )
        self.wait(1)
        self.play(FadeOut(death_group))

        # 3. 建物破壊率
        building_label = Text("リスボン市内の建物", font_size=36, color=YELLOW)
        building_value = Text("約85%が破壊", font_size=60, color=RED)
        building_group = VGroup(building_label, building_value).arrange(DOWN, buff=0.3)
        building_group.move_to(ORIGIN + UP * 1)

        self.play(FadeIn(building_label, shift=UP))
        self.play(Write(building_value))

        # 円グラフで視覚化
        pie_destroyed = Sector(
            radius=1.5,
            angle=0.85 * TAU,
            start_angle=PI / 2,
            color=RED,
            fill_opacity=0.8,
        )
        pie_remaining = Sector(
            radius=1.5,
            angle=0.15 * TAU,
            start_angle=PI / 2 + 0.85 * TAU,
            color=GREEN,
            fill_opacity=0.8,
        )
        pie_chart = VGroup(pie_destroyed, pie_remaining)
        pie_chart.move_to(DOWN * 1.5)

        # 凡例
        legend_destroyed = VGroup(
            Square(side_length=0.3, color=RED, fill_opacity=0.8),
            Text("破壊 85%", font_size=24),
        ).arrange(RIGHT, buff=0.2)
        legend_remaining = VGroup(
            Square(side_length=0.3, color=GREEN, fill_opacity=0.8),
            Text("残存 15%", font_size=24),
        ).arrange(RIGHT, buff=0.2)
        legend = VGroup(legend_destroyed, legend_remaining).arrange(DOWN, buff=0.2)
        legend.next_to(pie_chart, RIGHT, buff=1)

        self.play(
            Create(pie_destroyed),
            Create(pie_remaining),
            run_time=1.5,
        )
        self.play(FadeIn(legend))
        self.wait(2)

        # 最終まとめ
        self.play(
            FadeOut(building_group),
            FadeOut(pie_chart),
            FadeOut(legend),
        )

        # 全項目を一覧表示
        summary = VGroup(
            Text("• 推定マグニチュード: M8.5〜9", font_size=36),
            Text("• 死者数: 3万〜4万人", font_size=36),
            Text("• 建物の約85%が破壊", font_size=36),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary.move_to(ORIGIN)

        for item in summary:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)

        self.wait(2)


class DamageEstimationSimple(Scene):
    """シンプル版：テキストのみのアニメーション"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("被害想定", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 箇条書き項目
        items = [
            ("推定マグニチュード", "M8.5〜9", ORANGE),
            ("死者数", "3万〜4万人", RED),
            ("建物破壊率", "約85%", PURPLE),
        ]

        bullet_group = VGroup()

        for i, (label, value, color) in enumerate(items):
            # ラベル部分
            label_text = Text(f"• {label}:", font_size=36, color=GRAY_A)
            # 値部分
            value_text = Text(value, font_size=48, color=color)
            value_text.next_to(label_text, RIGHT, buff=0.3)

            item_group = VGroup(label_text, value_text)
            item_group.shift(DOWN * (i * 1.5) + UP * 1)

            bullet_group.add(item_group)

        # 順番にフェードイン
        for item in bullet_group:
            self.play(
                FadeIn(item[0], shift=RIGHT * 0.3),
                run_time=0.5,
            )
            self.play(
                FadeIn(item[1], scale=1.2),
                run_time=0.5,
            )
            self.wait(0.3)

        self.wait(2)

        # 強調アニメーション
        self.play(
            *[item[1].animate.set_color(YELLOW) for item in bullet_group],
            run_time=0.5,
        )
        self.play(
            bullet_group[0][1].animate.set_color(ORANGE),
            bullet_group[1][1].animate.set_color(RED),
            bullet_group[2][1].animate.set_color(PURPLE),
            run_time=0.5,
        )

        self.wait(1)


if __name__ == "__main__":
    # コマンドラインから実行する場合:
    # manim -pql damage_estimation_animation.py DamageEstimation
    # manim -pql damage_estimation_animation.py DamageEstimationSimple
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql damage_estimation_animation.py DamageEstimation")
    print("  manim -pql damage_estimation_animation.py DamageEstimationSimple")
