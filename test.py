from finngpu import load_gpu_models, match_gpu_model

gpu_models = load_gpu_models()
test_text = "Msi 2060 Gaming Z"
print(match_gpu_model(test_text, gpu_models, debug=True))
