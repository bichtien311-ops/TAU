import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "execution")))
from content_processor import clean_notebooklm_output

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

intro = """# ВВЕДЕНИЕ

Учебное пособие посвящено фундаментальным вопросам Теории автоматического управления (ТАУ) применительно к задачам электроэнергетики. Системы автоматического управления обеспечивают устойчивость, надежность и эффективность работы современных энергетических комплексов. Цель пособия — сформировать у обучающихся системное понимание математического аппарата, методов анализа динамических систем, а также практических аспектов работы автоматических регуляторов возбуждения (АРВ) генераторов. Материал пособия структурирован по модулям и охватывает темы от базовых дифференциальных уравнений до сложного частотного анализа и цифровых комплексов управления в энергосистемах. Каждая лекция содержит контрольные вопросы для закрепления материала.

# Модуль 1. Математический аппарат и теория линейных систем

"""

lec1 = read_file("d:/Antigravity/TAU/лекция1.md")
lec2 = read_file("d:/Antigravity/TAU/лекция2.md")
lec3 = read_file("d:/Antigravity/TAU/лекция3.md")
lec4_8 = read_file("d:/Antigravity/TAU/data/lectures_4_to_8.md")
lec9_13 = read_file("d:/Antigravity/TAU/data/lectures_9_to_13.md")
lec14_17 = read_file("d:/Antigravity/TAU/data/lectures_14_to_17.md")

final_text = intro + "\n\n".join([lec1, lec2, lec3, lec4_8, lec9_13, lec14_17])

# Clean text (removes artifacts, ensures correct GOST numbers)
cleaned_text = clean_notebooklm_output(final_text)

os.makedirs("d:/Antigravity/TAU/data", exist_ok=True)

with open("d:/Antigravity/TAU/data/master_tau.md", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Created data/master_tau.md successfully.")
