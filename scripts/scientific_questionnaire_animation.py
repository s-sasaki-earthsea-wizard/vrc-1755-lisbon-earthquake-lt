"""
科学的アンケート（Scientific Questionnaire）のManimアニメーション

ポンバル侯爵カルヴァーリョの科学的アンケートを視覚的に表現する：
- 「地震は何時に始まり、どれくらい続いたか？」
- 「海水は引いたか、満ちたか？高さはどの程度か？」
- 「建物の倒壊に方向性はあったか？」

マラグリダの「神罰説」との対比も表現
"""

from manim import *


class ScientificQuestionnaire(Scene):
    """科学的アンケートをアニメーション表示するシーン"""

    def construct(self):
        # 日本語フォント設定
        Text.set_default(font="Hiragino Sans")

        # タイトル: 二つの対照的な反応
        title = Text("二つの対照的な反応", font_size=56, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # 左側: マラグリダ（神罰説）
        left_name = Text("マラグリダ", font_size=32, color=RED)
        left_title = Text("(イエズス会宣教師)", font_size=20, color=GRAY_A)
        left_title.next_to(left_name, DOWN, buff=0.1)
        left_header = VGroup(left_name, left_title)
        left_header.move_to(LEFT * 3.5 + UP * 2)

        left_claim = Text("「市民の罪に対する\n神罰である」", font_size=28, color=RED_B)
        left_claim.set_line_spacing(1.2)
        left_claim.next_to(left_header, DOWN, buff=0.5)

        # 右側: ポンバル侯爵（科学的アンケート）
        right_name = Text("ポンバル侯爵", font_size=32, color=BLUE)
        right_title = Text("(宰相カルヴァーリョ)", font_size=20, color=GRAY_A)
        right_title.next_to(right_name, DOWN, buff=0.1)
        right_header = VGroup(right_name, right_title)
        right_header.move_to(RIGHT * 3.5 + UP * 2)

        right_label = Text("科学的アンケート", font_size=28, color=BLUE_B)
        right_label.next_to(right_header, DOWN, buff=0.5)

        # 中央の分割線
        divider = Line(
            start=UP * 1.5,
            end=DOWN * 3,
            color=GRAY,
            stroke_width=2,
        )

        # VS表示
        vs_text = Text("vs", font_size=36, color=YELLOW)
        vs_text.move_to(UP * 0.5)

        # 左右を表示
        self.play(
            FadeIn(left_header, shift=RIGHT),
            FadeIn(right_header, shift=LEFT),
        )
        self.play(Create(divider), Write(vs_text))
        self.play(
            FadeIn(left_claim, shift=UP),
            FadeIn(right_label, shift=UP),
        )
        self.wait(1)

        # 科学的アンケートの質問を順番に表示
        questions = [
            "「地震は何時に始まり、\n  どれくらい続いたか？」",
            "「海水は引いたか、満ちたか？\n  高さはどの程度か？」",
            "「建物の倒壊に\n  方向性はあったか？」",
        ]

        question_group = VGroup()
        for i, q in enumerate(questions):
            q_text = Text(q, font_size=22, color=WHITE)
            q_text.set_line_spacing(1.1)
            question_group.add(q_text)

        question_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        question_group.next_to(right_label, DOWN, buff=0.4)
        question_group.shift(LEFT * 0.5)

        for q in question_group:
            self.play(FadeIn(q, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.3)

        self.wait(1)

        # フェードアウト
        self.play(
            FadeOut(left_header),
            FadeOut(left_claim),
            FadeOut(right_header),
            FadeOut(right_label),
            FadeOut(question_group),
            FadeOut(divider),
            FadeOut(vs_text),
        )

        # 結論: 「なぜ」vs「どのように」
        conclusion = Text(
            "同じ災害に対する分岐点",
            font_size=40,
            color=WHITE,
        )
        conclusion.move_to(UP * 0.5)
        self.play(FadeIn(conclusion, shift=UP))

        why_text = Text("「なぜ」", font_size=48, color=RED)
        how_text = Text("「どのように」", font_size=48, color=BLUE)
        vs_text2 = Text("vs", font_size=32, color=YELLOW)

        comparison = VGroup(why_text, vs_text2, how_text).arrange(RIGHT, buff=0.5)
        comparison.move_to(DOWN * 1)

        self.play(
            FadeIn(why_text, shift=LEFT),
            Write(vs_text2),
            FadeIn(how_text, shift=RIGHT),
        )

        # 強調
        self.play(
            why_text.animate.scale(1.1),
            how_text.animate.scale(1.1),
            run_time=0.3,
        )
        self.play(
            why_text.animate.scale(1 / 1.1),
            how_text.animate.scale(1 / 1.1),
            run_time=0.3,
        )

        self.wait(2)


class ScientificQuestionnaireSimple(Scene):
    """シンプル版：アンケート質問のみ"""

    def construct(self):
        Text.set_default(font="Hiragino Sans")

        # タイトル
        title = Text("ポンバル侯爵の科学的アンケート", font_size=40, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # 質問リスト
        questions = [
            "「地震は何時に始まり、どれくらい続いたか？」",
            "「海水は引いたか、満ちたか？高さはどの程度か？」",
            "「建物の倒壊に方向性はあったか？」",
        ]

        q_group = VGroup()
        for i, q in enumerate(questions):
            icon = Text(f"Q{i+1}.", font_size=32, color=YELLOW)
            text = Text(q, font_size=28, color=WHITE)
            item = VGroup(icon, text).arrange(RIGHT, buff=0.3)
            q_group.add(item)

        q_group.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        q_group.move_to(UP * 0.3)

        for item in q_group:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.3)

        self.wait(1)

        # 補足: 全13項目
        note = Text("...など全13項目のアンケート調査", font_size=24, color=GRAY_A)
        note.move_to(DOWN * 2)
        self.play(FadeIn(note, shift=UP))

        self.wait(2)


if __name__ == "__main__":
    print("Manimアニメーションスクリプト")
    print("実行コマンド:")
    print("  manim -pql scientific_questionnaire_animation.py ScientificQuestionnaire")
    print("  manim -pql scientific_questionnaire_animation.py ScientificQuestionnaireSimple")
