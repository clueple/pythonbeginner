import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, WhisperProcessor, WhisperForConditionalGeneration
    return AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


@app.cell
def _(AutoModelForSeq2SeqLM, AutoTokenizer):
    checkpoint = r'facebook/nllb-200-distilled-600M'
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    return model, tokenizer


@app.cell
def _():
    target_lang = r'eng_Latn'
    source_lang = r'yue_Hant'
    return source_lang, target_lang


@app.cell
def _(model, pipeline, source_lang, target_lang, tokenizer):
    translator = pipeline(task='translation', model=model, tokenizer=tokenizer, src_lang= source_lang, tgt_lang= target_lang, max_length=400)
    return (translator,)


@app.cell
def _(translator):
    def get_trans(input_txt:str):
        output = translator(input_txt)
        translated_text = output[0]['translation_text']
        print(translated_text)
    return


@app.cell
def _(mo):
    t_src_txt = mo.ui.text_area(full_width=True, label='Cantonese To English',value='enter Cantonese here').form(submit_button_label='Confirm')
    t_src_txt
    return (t_src_txt,)


@app.cell
def _(t_src_txt):
    t_src_txt.value
    return


@app.cell
def _(t_src_txt, translator):
    tr = translator(t_src_txt.value)
    return (tr,)


@app.cell
def _(tr):
    tr[0]['translation_text']
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
