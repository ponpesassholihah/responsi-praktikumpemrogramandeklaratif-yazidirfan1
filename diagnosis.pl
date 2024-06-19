% diagnosis.pl
:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_json)).

% Gejala-gejala
gejala(perasaan_sedih).
gejala(kehilangan_minat).
gejala(gangguan_tidur).
gejala(perubahan_berat_badan).
gejala(pikiran_bunuh_diri).
gejala(perubahan_suasana_hati).
gejala(perubahan_pola_makan).
gejala(ketidakmampuan_konsentrasi).

% Diagnosa berdasarkan gejala
diagnosa(distimia, [perasaan_sedih]).
diagnosa(burnout, [kehilangan_minat]).
diagnosa(sleep_apnea, [gangguan_tidur]).
diagnosa(hipotiroidisme_atau_hipertiroidisme, [perubahan_berat_badan]).
diagnosa(ptsd, [pikiran_bunuh_diri]).
diagnosa(gangguan_siklotimik, [perubahan_suasana_hati]).
diagnosa(gangguan_nafsu_makan, [perubahan_pola_makan]).
diagnosa(gad, [ketidakmampuan_konsentrasi]).

% Aturan untuk menentukan diagnosa berdasarkan gejala
dapatkan_diagnosa(Gejala, Diagnosa) :-
    diagnosa(Diagnosa, DaftarGejala),
    subset(DaftarGejala, Gejala).

% Definisikan server
server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Endpoint untuk menerima permintaan diagnosa
:- http_handler('/diagnose', diagnose, []).

% Predikat untuk menangani permintaan diagnosa
diagnose(Request) :-
    http_read_json_dict(Request, Data),
    get_symptoms(Data.symptoms, Symptoms),
    find_diagnosis(Symptoms, Diagnosis, Recommendations),
    reply_json_dict(_{diagnosis: Diagnosis, recommendations: Recommendations}).

% Predikat untuk mengambil gejala dari permintaan
get_symptoms(SymptomsList, Symptoms) :-
    maplist(atom_string, Symptoms, SymptomsList).

% Predikat untuk menemukan diagnosa dan rekomendasi
find_diagnosis(Symptoms, Diagnosis, Recommendations) :-
    findall(Diagnosis, dapatkan_diagnosa(Symptoms, Diagnosis), Diagnoses),
    % Asumsikan satu diagnosa untuk kesederhanaan, bisa dikembangkan untuk multiple diagnosis
    Diagnoses = [Diagnosis | _],
    recommendations(Diagnosis, Recommendations).

% Rekomendasi berdasarkan diagnosa
recommendations(distimia, "Lakukan aktivitas yang menyenangkan, berbicara dengan teman atau keluarga, atau berkonsultasi dengan profesional jika diperlukan.").
recommendations(burnout, "Coba kegiatan baru, berolahraga, atau mencari hobi baru untuk menemukan kembali minat dan kegembiraan.").
recommendations(sleep_apnea, "Buat rutinitas tidur yang teratur, hindari kafein sebelum tidur, dan coba teknik relaksasi sebelum tidur.").
recommendations(hipotiroidisme_atau_hipertiroidisme, "Konsultasi dengan ahli gizi, atur pola makan sehat, dan perhatikan asupan kalori harian.").
recommendations(ptsd, "Segera cari bantuan profesional, bicarakan dengan orang yang dipercaya, dan hindari isolasi diri.").
recommendations(gangguan_siklotimik, "Catat suasana hati harian, hindari stres, dan coba teknik manajemen stres seperti meditasi atau yoga.").
recommendations(gangguan_nafsu_makan, "Makan makanan sehat, jadwalkan waktu makan teratur, dan hindari makanan yang terlalu banyak gula atau lemak.").
recommendations(gad, "Buat jadwal, atur prioritas tugas, dan coba teknik fokus seperti time-blocking atau metode Pomodoro.").