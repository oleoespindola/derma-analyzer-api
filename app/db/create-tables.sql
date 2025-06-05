-- PERFIS

create table profiles (
	id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE cascade,
	name text not null
);

-- REGRAS PARA VIZUALIZAÇÃO DOS DADOS DE PERFIS

-- Vizualizar dados
CREATE POLICY "Can read own profile"
ON profiles
FOR SELECT
USING (auth.uid() = id);

-- Inserir dados
CREATE POLICY "Can insert own profile"
ON profiles
FOR INSERT
WITH CHECK (auth.uid() = id);

-- Atualizar dados
CREATE POLICY "Can update own profile"
ON profiles
FOR UPDATE
USING (auth.uid() = id);


-- CRIAÇÃO DA TABELA DE RESULTADO DAS ANÁLISES

CREATE TABLE image_analysis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    analysis_result TEXT,
    user_feedback TEXT,
    feedback_timestamp TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);

-- REGRAS PARA VIZUALIZAÇÃO DOS DADOS DAS ANÁLISES

-- Vizualizar análises
CREATE POLICY "Can read own images"
ON image_analysis
FOR SELECT
USING (auth.uid() = user_id);

-- Inserir análises 
CREATE POLICY "Can insert own images"
ON image_analysis
FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- Atualizar análises 
CREATE POLICY "Can update own images"
ON image_analysis
FOR UPDATE
USING (auth.uid() = user_id);

-- Sotorage (private) configurado no supabase para ARMAZENAMENTO DAS IMAGENS ANALIZADAS

-- REGRAS PARA VIZUALIZAÇÃO DAS IMAGENS

-- Vizualizar imagens
CREATE POLICY "Allow users to view their own files"
ON storage.objects
FOR SELECT
USING (auth.uid()::text = split_part(name, '/', 1));

-- Inserir imagens
CREATE POLICY "Allow users to upload files to their own folder"
ON storage.objects
FOR INSERT
WITH CHECK (auth.uid()::text = split_part(name, '/', 1));

