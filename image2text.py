
# coding: utf-8
# Copyright [zashio]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import Image, ImageDraw, ImageFont
import sys
import pyocr
import pyocr.builders
import argparse


def extract_word_box(filepath, use_lang_num = 0):
    tool = pyocr.get_available_tools()[0]
    use_lang = tool.get_available_languages()[use_lang_num]

    image = Image.open(filepath)
    image = image.convert("L")
    image = image.point(lambda x: 0 if x < 128 else x) 
    image = Image.merge(
        "RGB",
        (   
            image.point(lambda x: x),
            image.point(lambda x: x),
            image.point(lambda x: x)
        )
    )

    word_boxes = tool.image_to_string(
        image,
        lang=use_lang,
        builder=pyocr.builders.WordBoxBuilder()
    )

    return image, word_boxes


def draw_boxes(image, word_boxes, color):
    """長方形の左上と右下の頂点を受け取り画像に描画する"""
    draw = ImageDraw.Draw(image)

    for word_box in word_boxes:
        
        pos1_x = word_box.position[0][0]
        pos1_y = word_box.position[0][1]
        pos2_x = word_box.position[1][0]
        pos2_y = word_box.position[1][1]
        
        draw.polygon([
            pos1_x, pos1_y,
            pos2_x, pos1_y,
            pos2_x, pos2_y,
            pos1_x, pos2_y], None, color)
            
    return image


def draw_texts(image, word_boxes, color):
    draw = ImageDraw.Draw(image)

    fnt = ImageFont.truetype('resource/Kokoro.otf',30)

#    日本語文を扱う場合には、上記のようにフォントを設定する必要がある
#    draw.text()の引数に、font=fntを追加する。
    
    for word_box in word_boxes:
        
        pos1_x = word_box.position[0][0]
        pos2_y = word_box.position[1][1]
    
        draw_position = (pos1_x, pos2_y)
        
        content = word_box.content
        
        draw.text(draw_position, content, color, font=fnt)
        
    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'filepath', help='文字認識を行う画像ファイルへのパスを入力')
    args = parser.parse_args()

    filepath = args.filepath

    #日本語文字認識を行いたいときは引数に、use_lang = 1を追加してください。
    image, word_boxes = extract_word_box(filepath)

    draw_boxes(image, word_boxes, 'Red')
    draw_texts(image, word_boxes, 'blue')

    image.save('resource/Out.png')