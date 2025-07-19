# 手順メモ
- .github/workflows 以下にワークフローの yaml を追加
- .gitmodules を追加
- Actions に書き込み権限を付与する
   - Settings > Actions > Generals を開く
   - "Workflow permissions" の項目から "Read and write permissions" を選択する
- Github pages にデプロイするファイル群を設定する
   - Settings > Pages を開く
   - "Build and deployment" の項目を以下の通りに設定する 
      - "Source" を "Deploy from a branch" に設定する
      -"Branch" を "gh-pages"、ディレクトリを "/ (root)" に設定し、保存する

#
- テーマの更新
   - layouts 以下にカスタマイズしたテンプレートを配置すればよい
