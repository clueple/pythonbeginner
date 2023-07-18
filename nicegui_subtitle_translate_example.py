"""python packages needed"""
from nicegui import ui, events
from deep_translator import GoogleTranslator as gt


"""click events"""
def handle_upload(e: events.UploadEventArguments):
    """ When uploading a file, the preview element preview the file content """
    preview.clear()
    prev_txt = e.content.read().decode('utf-8')
    preview.set_value(prev_txt)
    preview.update()
    # change the 'result' element for your case
    result.set_value(preview.value)


"""upload area"""
src_file = ui.upload(auto_upload=True, on_upload=handle_upload)

# text area to preview uploaded content
preview = ui.textarea(label="Uploaded Content").props('clearable').style("width: 75%; height:200px ; border:solid 1px orange; resize: none; padding: 12px 12px")

# text are
result = ui.textarea(label="Translated Content").props('clearable').style("width: 75%; height:200px ; border:solid 1px orange; resize: none; padding: 12px 12px")

# ui.run(native=True, reload=False)
ui.run()
