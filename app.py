# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # 启用CORS以允许前端访问

# 确保存储数据的目录存在
DATA_DIR = 'survey_data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


@app.route('/api/submit', methods=['POST'])
def submit_survey():
    try:
        # 获取问卷数据
        survey_data = request.json

        # 添加提交时间戳
        survey_data['submission_time'] = datetime.now().isoformat()

        # 生成唯一的文件名（使用时间戳）
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{survey_data.get('name', 'anonymous')}.json"
        file_path = os.path.join(DATA_DIR, filename)

        # 保存数据到文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(survey_data, f, ensure_ascii=False, indent=2)

        return jsonify({
            'status': 'success',
            'message': '问卷提交成功',
            'survey_id': filename
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'提交失败: {str(e)}'
        }), 500


@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    try:
        surveys = []
        for filename in os.listdir(DATA_DIR):
            if filename.endswith('.json'):
                with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as f:
                    survey_data = json.load(f)
                    surveys.append(survey_data)

        return jsonify({
            'status': 'success',
            'surveys': surveys
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'获取数据失败: {str(e)}'
        }), 500


@app.route('/api/survey/<survey_id>', methods=['GET'])
def get_survey(survey_id):
    try:
        file_path = os.path.join(DATA_DIR, survey_id)
        if not os.path.exists(file_path):
            return jsonify({
                'status': 'error',
                'message': '问卷不存在'
            }), 404

        with open(file_path, 'r', encoding='utf-8') as f:
            survey_data = json.load(f)

        return jsonify({
            'status': 'success',
            'survey': survey_data
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'获取数据失败: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)