import os.path

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram import types
from answers import CallbackOnStart
from keyboard import kb

result = []
module = 0
points_for_emotional_exhaustion = []
points_for_depersonalization = []
points_for_the_reduction_of_professionalism = []


@dp.message_handler(Command("on_start_burnout_test"))
async def on_start_test(message: types.Message, state: FSMContext):
    path = "./test_burnout.txt"
    check_file = os.path.isfile(path)
    if check_file:
        result.append(message.from_user.id)
        await message.answer("Данный опрос предназначен для диагностики профессионального выгорания и был разработан"
                             " Кристиной Маслач и Сьюзан Джексон в 1986 году.\nНапишите /start для начала теста")
        await CallbackOnStart.Q1.set()
    else:
        await message.answer("Упс, один из файлов не найден, обратитесь в поддержку")
        await state.finish()


@dp.message_handler(state=CallbackOnStart.Q0)
async def question(message: types.Message):
    await message.answer("Кем вы работаете?")
    result.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q1)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №1\nЯ чувствую себя эмоционально опустошенным\nВыберите по шкале от 0 до 6, где 0 это 'Не чувствую совсем себя опустошенным', а 6 'Постоянно чувствую себя опустошенным'",
        reply_markup=kb)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q2)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №2\nПосле работы я чувствую себя как 'выжатый лимон'",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q3)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №3\nУтром я чувствую усталость и не желание идти на работу ",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q4)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №4\nЯ хорошо понимаю, что чувствуют мои подчиненные и коллеги, и стараюсь учитывать это в интересах дела",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q5)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №5\nЯ чувствую, что общаюсь с некоторыми подчиненными и коллегами как с предметами (без теплоты и расположения к ним)",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q6)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №6\nПосле работы на некоторое время хочется уединиться от всех и всего",
        reply_markup=kb)
    points_for_depersonalization.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q7)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №7\nЯ умею находить правильное решение в конфликтных ситуациях, возникающих при общении с коллегами",
        reply_markup=kb)
    module = (int(message.text) - 6) * (-1)
    points_for_emotional_exhaustion.append(module)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q8)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №8\nЯ чувствую угнетенность и апатию",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q9)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №9\nЯ уверен, что моя работа нужна людям",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q10)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №10\nВ последнее время я стал более «черствым» по отношению к тем, с кем работаю",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q11)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №11\nЯ замечаю, что моя работа ожесточает меня",
        reply_markup=kb)
    points_for_depersonalization.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q12)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №12\nУ меня много планов на будущее, и я верю в их осуществление",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q13)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №13\nМоя работа все больше меня разочаровывает",
        reply_markup=kb)
    points_for_depersonalization.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q14)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №14\nМне кажется, что я слишком много работаю",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q15)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №15\nБывает, что мне действительно безразлично то, что происходит c некоторыми моими подчиненными и коллегами",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q16)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №16\nМне хочется уединиться и отдохнуть от всего и всех",
        reply_markup=kb)
    points_for_depersonalization.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q17)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №17\nЯ легко могу создать атмосферу доброжелательности и сотрудничества в коллективе",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q18)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №18\nВо время работы я чувствую приятное оживление",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q19)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №19\nБлагодаря своей работе я уже сделал в жизни много действительно ценного",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q20)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №20\nЯ чувствую равнодушие и потерю интереса ко многому, что радовало меня в моей работе",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q21)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №21\nНа работе я спокойно справляюсь с эмоциональными проблемами",
        reply_markup=kb)
    points_for_emotional_exhaustion.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q22)
async def question(message: types.Message):
    await message.answer(
        text="Вопрос №22\nВ последнее время мне кажется, что коллеги и подчиненные все чаще перекладывают на меня груз своих проблем и обязанностей",
        reply_markup=kb)
    points_for_the_reduction_of_professionalism.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q23)
async def end(message: types.Message, state: FSMContext):
    points_for_depersonalization.append(message.text)
    await message.answer(text="Ваш результат:", reply_markup=ReplyKeyboardRemove())
    emotional_exhaustion = [int(s) for s in points_for_emotional_exhaustion]
    emotional_exhaustion = sum(emotional_exhaustion)
    depersonalization = [int(s) for s in points_for_depersonalization]
    depersonalization = sum(depersonalization)
    reduction_of_professionalism = [int(s) for s in points_for_the_reduction_of_professionalism]
    reduction_of_professionalism = sum(reduction_of_professionalism)
    await message.answer("«Эмоциональное истощение» проявляется в переживаниях, утраты интереса и позитивных "
                         "чувств к окружающим, ощущении «пресыщенности» работой, неудовлетворенностью жизнью в целом. "
                         "В контексте синдрома перегорания «деперсонализация» предполагает формирование особых, "
                         "деструктивных взаимоотношений с окружающими людьми.")
    if (emotional_exhaustion < 16):
        await message.answer("У вас эмоциональное истощение на низком  уровне")
    elif (emotional_exhaustion > 15) and (emotional_exhaustion < 25):
        await message.answer("У вас эмоциональное истощение на среднем уровне")
    else:
        await message.answer("У вас эмоциональное истощение на высоком уровне")
    await message.answer("«Деперсонализация» проявляется в эмоциональном отстранении и безразличии, формальном "
                         "выполнении профессиональных обязанностей без личностной включенности и сопереживания, а в "
                         "отдельных случаях – в негативизме и циничном отношении. На поведенческом уровне "
                         "«деперсонализация» проявляется в высокомерном поведении, использовании профессионального "
                         "сленга, юмора, ярлыков.")
    if (depersonalization < 6):
        await message.answer("Ваша деперсонализация на низком уровне")
    elif (depersonalization > 5) and (depersonalization < 11):
        await message.answer("Ваша деперсонализация на среднем уровне")
    else:
        await message.answer("Ваша деперсонализация на высоком уровне")
    await message.answer("«Редукция профессиональных достижений» отражает степень удовлетворенности "
                         "работника собой как личностью и как профессионалом. Неудовлетворительное значение этого "
                         "показателя отражает тенденцию к негативной оценке своей компетентности и продуктивности и,"
                         " как следствие, - снижение профессиональной мотивации, нарастание негативизма в отношении "
                         "служебных обязанностей, тенденцию к снятию с себя ответственности, к изоляции от окружающих, "
                         "отстраненность и неучастие, избегание работы сначала психологически, а затем физически.")
    if (reduction_of_professionalism > 36):
        await message.answer("Редукция профессиональных достижений у вас на низком уровне")
    elif (reduction_of_professionalism > 30) and (reduction_of_professionalism < 37):
        await message.answer("Редукция профессиональных достижений у вас на среднем уровне")
    else:
        await message.answer("Редукция профессиональных достижений у вас на высоком уровне")
    result.append(emotional_exhaustion)
    result.append(depersonalization)
    result.append(reduction_of_professionalism)
    with open("test_burnout.txt", "w") as file:
        file.write(str(result))
        file.close()
    await state.finish()
