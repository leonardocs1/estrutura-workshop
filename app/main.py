from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':
    # Caminho do arquivo Excel
    input_path = 'data/input'
    output_path = 'data/output'
    file_name = 'dados'

    # Extrair dados do Excel
    data_frame = extract_from_excel(input_path)

    # Transformar os dados (exemplo: concatenar DataFrames)
    transformed_data_frame = concat_data_frames(data_frame)

    # Carregar os dados transformados de volta para um arquivo Excel
    result_message = load_excel(transformed_data_frame, output_path, file_name)

    print(result_message)  # Exibir mensagem de sucesso
