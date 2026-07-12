from google import genai

API_KEY = ""

client = genai.Client(api_key = API_KEY)

artikel_mentah  = """
Kecerdasan Buatan (AI) adalah simulasi kecerdasan manusia yang dimodelkan 
di dalam mesin dan diprogram agar bisa berpikir seperti halnya manusia. 
Sedangkan menurut Mc Leod dan Schell, kecerdasan buatan adalah aktivitas 
penyediaan mesin seperti komputer dengan kemampuan untuk menampilkan 
perilaku yang dianggap sama cerdasnya dengan jika kemampuan tersebut 
ditampilkan oleh manusia. Teknologi ini semakin hari semakin berkembang 
pesat dan mulai merambah ke berbagai sektor, mulai dari pendidikan, 
kesehatan, hingga industri otomotif.
"""

prompt_instruksi = f"""
Tugasmu adalah meringkas teks artikel di bawah ini.
Aturan yang WAJIB dipatuhi:
- Ringkas menjadi tepat 2 poin utama (bullet points)
- Gunakan bahasa yang santai namun profesional
- Jangan tambahkan opini pribadimu

teks artikel :
{artikel_mentah}
"""

print("sedang memproses ringkasan... Mohon tunggu sebentar")

try :
    respons = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_instruksi)
    
    print("=== Hasil Ringkasan Artikel ===")
    print(respons.text)
    
except Exception as e:
    print(f"terjadi kesalahan saat memproses data : {e}")

