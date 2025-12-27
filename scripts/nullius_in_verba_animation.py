"""
Nullius in verba（権威を鵜呑みにするな）のManimアニメーション

英国王立協会（1660年設立）のモットーを視覚的に表現する
"""

from manim import *


class NulliusInVerba(Scene):
    """Nullius in verbaをアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # 背景的な装飾（王立協会を象徴）
        emblem = Circle(radius=2.5, color=GOLD, stroke_width=2, stroke_opacity=0.3)
        self.play(Create(emblem), run_time=1)

        # メインのラテン語テキスト
        latin_text = Text(
            "Nullius in verba",
            font_size=72,
            color=GOLD,
        )
        latin_text.move_to(UP * 0.5)

        # 文字を1文字ずつ表示
        self.play(Write(latin_text), run_time=2)
        self.wait(0.5)

        # 下線を引く
        underline = Line(
            start=latin_text.get_left() + DOWN * 0.3,
            end=latin_text.get_right() + DOWN * 0.3,
            color=GOLD,
            stroke_width=2,
        )
        self.play(Create(underline), run_time=0.5)

        # 日本語訳を表示
        japanese_text = Text(
            "「権威を鵜呑みにするな」",
            font_size=48,
            color=WHITE,
        )
        japanese_text.next_to(underline, DOWN, buff=0.5)

        self.play(FadeIn(japanese_text, shift=UP), run_time=1)
        self.wait(1)

        # 補足情報
        info = Text(
            "— 英国王立協会モットー (1660年)",
            font_size=28,
            color=GRAY_A,
        )
        info.next_to(japanese_text, DOWN, buff=0.5)

        self.play(FadeIn(info, shift=UP), run_time=0.8)

        # 強調アニメーション
        self.wait(0.5)
        self.play(
            latin_text.animate.set_color(YELLOW),
            run_time=0.5,
        )
        self.play(
            latin_text.animate.set_color(GOLD),
            run_time=0.5,
        )

        self.wait(2)

        # フェードアウト
        self.play(
            FadeOut(emblem),
            FadeOut(latin_text),
            FadeOut(underline),
            FadeOut(japanese_text),
            FadeOut(info),
        )


class NulliusInVerbaSimple(Scene):
    """シンプル版"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # ラテン語
        latin = Text("Nullius in verba", font_size=64, color=GOLD)

        # 日本語訳
        japanese = Text("「権威を鵜呑みにするな」", font_size=40, color=WHITE)
        japanese.next_to(latin, DOWN, buff=0.5)

        group = VGroup(latin, japanese)
        group.move_to(ORIGIN)

        self.play(Write(latin), run_time=1.5)
        self.play(FadeIn(japanese, shift=UP), run_time=0.8)
        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql nullius_in_verba_animation.py NulliusInVerba")
    print("  manim -pql nullius_in_verba_animation.py NulliusInVerbaSimple")
